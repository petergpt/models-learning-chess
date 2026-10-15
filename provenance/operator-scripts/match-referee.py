#!/usr/bin/env python3
"""Neutral, durable head-to-head referee. No chess engine, evaluations or search."""
from pathlib import Path
import argparse
from contextlib import contextmanager
import datetime as dt
import hashlib
import hmac
import json
import secrets
import sqlite3
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
MATCH = ROOT / 'Matches/Astra vs Opus - 30 games'
sys.path.insert(0, str(MATCH / '.referee/vendor'))
import chess

def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def encode(value): return json.dumps(value, sort_keys=True, separators=(',', ':'))
def digest(value): return hashlib.sha256(encode(value).encode()).hexdigest()
LABELS = {'astra': 'GPT-6 Astra', 'opus': 'Claude Opus 5.5'}

class Fault(Exception):
    def __init__(self, message, status=409): self.message, self.status = message, status

class Referee:
    def __init__(self, folder=MATCH):
        self.folder = Path(folder)
        self.path = self.folder / '.referee/match.sqlite'
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS games(id INTEGER PRIMARY KEY,white TEXT NOT NULL,black TEXT NOT NULL,
                  started TEXT NOT NULL,ended TEXT,result TEXT,reason TEXT,moves TEXT NOT NULL DEFAULT '[]',
                  illegal_count INTEGER NOT NULL DEFAULT 0,draw_offer TEXT);
                CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT,at TEXT NOT NULL,
                  kind TEXT NOT NULL,game INTEGER,actor TEXT,payload TEXT NOT NULL,previous TEXT NOT NULL,hash TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS actions(id TEXT PRIMARY KEY,actor TEXT NOT NULL,request TEXT NOT NULL,receipt TEXT NOT NULL);
            ''')
            if not db.execute("SELECT 1 FROM meta WHERE key='status'").fetchone():
                protocol = json.loads((self.folder / 'protocol.json').read_text())
                self.set_meta(db, 'protocol', protocol)
                self.set_meta(db, 'status', 'ready')
                self.set_meta(db, 'createdAt', now())
                self.event(db, 'match_created', None, None, {'protocolSha256': digest(protocol)})

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=20)
        db.row_factory = sqlite3.Row
        try:
            db.execute('PRAGMA journal_mode=WAL'); db.execute('PRAGMA synchronous=FULL')
            with db: yield db
        finally: db.close()
    def meta(self, db, key):
        row = db.execute('SELECT value FROM meta WHERE key=?', (key,)).fetchone()
        return json.loads(row[0]) if row else None
    def set_meta(self, db, key, value):
        db.execute('INSERT INTO meta VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value', (key, encode(value)))
    def event(self, db, kind, game, actor, payload):
        row = db.execute('SELECT hash FROM events ORDER BY seq DESC LIMIT 1').fetchone()
        prev = row[0] if row else '0' * 64
        value = {'at': now(), 'kind': kind, 'game': game, 'actor': actor, 'payload': payload, 'previous': prev}
        db.execute('INSERT INTO events(at,kind,game,actor,payload,previous,hash) VALUES(?,?,?,?,?,?,?)',
            (value['at'], kind, game, actor, encode(payload), prev, digest(value)))
    @staticmethod
    def board(game):
        board = chess.Board()
        for move in json.loads(game['moves']): board.push_uci(move['uci'])
        return board
    @staticmethod
    def token(game, board): return f"{game['id']}:{board.ply()}:{hashlib.sha256(board.fen().encode()).hexdigest()[:24]}"
    def current(self, db): return db.execute('SELECT * FROM games ORDER BY id DESC LIMIT 1').fetchone()
    def score(self, db):
        score = {'astra': 0, 'opus': 0}; wins = {'astra': 0, 'opus': 0}; draws = 0; count = 0
        for g in db.execute('SELECT * FROM games WHERE result IS NOT NULL'):
            if g['result'] == '*': continue
            count += 1
            if g['result'] == '1/2-1/2':
                score['astra'] += .5; score['opus'] += .5; draws += 1
            else:
                winner = g['white'] if g['result'] == '1-0' else g['black']
                score[winner] += 1; wins[winner] += 1
        return {'points': score, 'wins': wins, 'draws': draws, 'completed': count, 'total': 30}
    def state(self, actor=None):
        with self.connect() as db:
            db.execute('BEGIN')
            return self._state(db, actor)
    def _state(self, db, actor=None):
        g = self.current(db)
        result = {'match': 'astra-opus-30', 'status': self.meta(db, 'status'), 'score': self.score(db),
                  'you': actor, 'label': LABELS.get(actor), 'game': None}
        if not g: return result
        b = self.board(g); turn = g['white'] if b.turn else g['black']
        result.update(game=g['id'], white=g['white'], black=g['black'], fen=b.fen(),
            turn=turn if not g['ended'] else None, yourTurn=bool(actor == turn and not g['ended'] and result['status'] == 'playing'),
            ply=b.ply(), positionToken=self.token(g,b), moves=' '.join(m['san'] for m in json.loads(g['moves'])),
            uci=' '.join(m['uci'] for m in json.loads(g['moves'])), result=g['result'], reason=g['reason'],
            check=b.is_check(), drawOffer=g['draw_offer'], illegalAttempts=g['illegal_count'],
            board=str(b))
        return result
    def start_game(self):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            g = self.current(db); status = self.meta(db,'status')
            if g and not g['ended']: return g['id']
            if status in ['paused','unfinished']: raise Fault('Match requires operator review before continuing')
            i = (g['id'] if g else 0) + 1
            if i > 30: raise Fault('The 30-game match is complete')
            protocol = self.meta(db,'protocol'); white = protocol['firstWhite'] if i % 2 else ('opus' if protocol['firstWhite'] == 'astra' else 'astra')
            black = 'opus' if white == 'astra' else 'astra'
            db.execute('INSERT INTO games(id,white,black,started) VALUES(?,?,?,?)', (i,white,black,now()))
            self.set_meta(db,'status','playing')
            if i == 1: self.set_meta(db,'startedAt',now())
            self.event(db,'game_started',i,None,{'white':white,'black':black,'initialFen':chess.STARTING_FEN})
            return i
    def finish(self, db, g, result, reason, actor=None):
        db.execute('UPDATE games SET ended=?,result=?,reason=? WHERE id=?', (now(),result,reason,g['id']))
        self.event(db,'game_ended',g['id'],actor,{'result':result,'reason':reason,'fen':self.board(g).fen()})
        self.set_meta(db,'status', 'unfinished' if result == '*' else ('complete' if g['id'] == 30 else 'between_games'))
        if g['id'] == 30 and result != '*': self.set_meta(db,'endedAt',now())
    def act(self, actor, action):
        if actor not in LABELS: raise Fault('Unknown player',403)
        if set(action) - {'id','command','positionToken','uci','note'}: raise Fault('Unknown action fields',400)
        if not isinstance(action.get('id'),str) or not 10 <= len(action['id']) <= 80: raise Fault('Action id is required',400)
        if action.get('command') not in ('move','resign','offer_draw','accept_draw'): raise Fault('Unknown command',400)
        if not isinstance(action.get('note',''),str) or len(action.get('note','')) > 240: raise Fault('Comment exceeds 240 characters',400)
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            prior = db.execute('SELECT * FROM actions WHERE id=?',(action['id'],)).fetchone()
            if prior:
                if prior['actor'] != actor or prior['request'] != encode(action): raise Fault('Action id reused with different content')
                return {'receipt':json.loads(prior['receipt']),'state':self._state(db,actor),'duplicate':True}
            g = self.current(db)
            if not g or g['ended'] or self.meta(db,'status') != 'playing': raise Fault('No active game')
            b = self.board(g)
            if action.get('positionToken') != self.token(g,b): raise Fault('Position changed. Run ./play board before submitting.')
            turn = g['white'] if b.turn else g['black']
            if turn != actor: raise Fault('It is the other player’s turn')
            command = action['command']; receipt = {'accepted':True,'command':command,'game':g['id'],'plyBefore':b.ply()}
            if command == 'move':
                uci = action.get('uci'); move = None
                try:
                    if isinstance(uci,str): move = chess.Move.from_uci(uci)
                except ValueError: pass
                if move is None or move not in b.legal_moves:
                    n = g['illegal_count'] + 1
                    db.execute('UPDATE games SET illegal_count=? WHERE id=?',(n,g['id']))
                    self.event(db,'illegal_submission',g['id'],actor,{'uci':str(uci)[:12],'ply':b.ply(),'count':n})
                    receipt.update(accepted=False,error='Illegal move',illegalAttempts=n)
                    if n >= 3: self.finish(db,g,'0-1' if b.turn else '1-0','illegal_move_forfeit',actor)
                else:
                    san = b.san(move); b.push(move)
                    moves = json.loads(g['moves']); moves.append({'uci':uci,'san':san,'actor':actor,'at':now()})
                    # Any draw offer is declined by the opponent making a move.
                    offer = g['draw_offer'] if g['draw_offer'] == actor else None
                    db.execute('UPDATE games SET moves=?,illegal_count=0,draw_offer=? WHERE id=?',(encode(moves),offer,g['id']))
                    self.event(db,'move',g['id'],actor,{'uci':uci,'san':san,'ply':b.ply(),'fen':b.fen(), 'note':action.get('note','')})
                    g = self.current(db); receipt.update(uci=uci,san=san,plyAfter=b.ply())
                    outcome = b.outcome()
                    if outcome:
                        reason = outcome.termination.name.lower()
                        self.finish(db,g,outcome.result(),reason,actor)
                    elif b.is_repetition(3): self.finish(db,g,'1/2-1/2','threefold_repetition',actor)
                    elif b.is_fifty_moves(): self.finish(db,g,'1/2-1/2','fifty_moves',actor)
                    elif b.ply() >= 400: self.finish(db,g,'*','safety_limit',actor)
            elif command == 'resign': self.finish(db,g,'0-1' if b.turn else '1-0','resignation',actor)
            elif command == 'offer_draw':
                db.execute('UPDATE games SET draw_offer=? WHERE id=?',(actor,g['id']))
                self.event(db,'draw_offered',g['id'],actor,{'ply':b.ply()})
            elif command == 'accept_draw':
                if not g['draw_offer'] or g['draw_offer'] == actor: raise Fault('No opponent draw offer')
                self.finish(db,g,'1/2-1/2','agreement',actor)
            db.execute('INSERT INTO actions VALUES(?,?,?,?)',(action['id'],actor,encode(action),encode(receipt)))
            return {'receipt':receipt,'state':self._state(db,actor),'duplicate':False}
    def public(self):
        with self.connect() as db:
            db.execute('BEGIN')
            state = self._state(db)
            games = []
            for row in db.execute('SELECT * FROM games ORDER BY id'):
                g = dict(row); b = self.board(g); moves = json.loads(g['moves'])
                games.append({k:g[k] for k in ['id','white','black','started','ended','result','reason']} |
                    {'uci':' '.join(m['uci'] for m in moves),'san':' '.join(m['san'] for m in moves),'fen':b.fen(),'ply':b.ply()})
            head = db.execute('SELECT seq,hash FROM events ORDER BY seq DESC LIMIT 1').fetchone()
            return {'id':'astra-opus-30','title':'Astra vs Opus','status':state['status'],
                'players':{id:{'label':label,'reasoning':'max','sourceGames':200} for id,label in LABELS.items()},
                'format':{'games':30,'colorsEach':15,'firstWhite':self.meta(db,'protocol')['firstWhite']},
                'score':state['score'],'currentGame':state['game'],'turn':state.get('turn'),
                'createdAt':self.meta(db,'createdAt'),'startedAt':self.meta(db,'startedAt'),'endedAt':self.meta(db,'endedAt'),
                'games':games,'eventSequence':head['seq'],'ledgerHead':head['hash']}
    def verify(self):
        with self.connect() as db:
            db.execute('BEGIN')
            prev = '0'*64
            recorded={}
            for row in db.execute('SELECT * FROM events ORDER BY seq'):
                value={k:row[k] for k in ['at','kind','game','actor','previous']};value['payload']=json.loads(row['payload'])
                if row['previous'] != prev or row['hash'] != digest(value): raise Fault('Audit chain mismatch')
                prev = row['hash']
                p=value['payload'];id=row['game']
                if row['kind']=='match_created':assert p['protocolSha256']==digest(self.meta(db,'protocol'))
                if row['kind']=='game_started':recorded[id]={'white':p['white'],'black':p['black'],'moves':[],'end':None}
                if row['kind']=='move':recorded[id]['moves'].append((p['uci'],p['san'],row['actor']))
                if row['kind']=='game_ended':recorded[id]['end']=p
            for row in db.execute('SELECT * FROM games'):
                b=chess.Board()
                for m in json.loads(row['moves']):
                    move=chess.Move.from_uci(m['uci'])
                    assert move in b.legal_moves and b.san(move)==m['san']
                    assert m['actor']==(row['white'] if b.turn else row['black'])
                    b.push(move)
                record=recorded[row['id']]
                assert (record['white'],record['black'])==(row['white'],row['black'])
                assert record['moves']==[(m['uci'],m['san'],m['actor']) for m in json.loads(row['moves'])]
                if row['ended']:
                    assert record['end'] and (record['end']['result'],record['end']['reason'],record['end']['fen'])==(row['result'],row['reason'],b.fen())
                else:assert record['end'] is None and row['result'] is None
            return {'ok':True,'ledgerHead':prev,'games':db.execute('SELECT count(*) FROM games').fetchone()[0]}

class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def send(self,status,value):
        body=encode(value).encode();self.send_response(status)
        self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(body)))
        self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(body)
    def actor(self):
        supplied=self.headers.get('Authorization','').removeprefix('Bearer ')
        for id,token in self.server.tokens.items():
            if hmac.compare_digest(supplied,token): return id
        raise Fault('Unauthorized',401)
    def do_GET(self):
        try:
            if urlsplit(self.path).path != '/state': raise Fault('Not found',404)
            self.send(200,self.server.referee.state(self.actor()))
        except Fault as e:self.send(e.status,{'error':e.message})
    def do_POST(self):
        try:
            if urlsplit(self.path).path != '/action': raise Fault('Not found',404)
            actor=self.actor();length=int(self.headers.get('Content-Length','0'))
            if not 0 < length <= 4096: raise Fault('Invalid action size',413)
            action=json.loads(self.rfile.read(length))
            if not isinstance(action,dict): raise Fault('Object required',400)
            self.send(200,self.server.referee.act(actor,action))
        except Fault as e:self.send(e.status,{'error':e.message})
        except (ValueError,TypeError):self.send(400,{'error':'Invalid JSON action'})

def serve():
    tokens=json.loads((MATCH/'.referee/tokens.json').read_text())
    server=ThreadingHTTPServer(('127.0.0.1',8776),Handler);server.daemon_threads=True
    server.tokens=tokens;server.referee=Referee();server.serve_forever()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['serve','start','public','verify']);args=parser.parse_args()
    if args.command=='serve':serve()
    elif args.command=='start': print(Referee().start_game())
    elif args.command=='public': print(encode(Referee().public()))
    else: print(encode(Referee().verify()))
