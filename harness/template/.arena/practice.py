"""Recorded, learner-selected opponent practice. Never contributes to benchmark Elo."""
import argparse
import datetime as dt
import fcntl
import gzip
import hashlib
import json
import os
import time


class Practice:
    def __init__(self, arena):
        self.a = arena
        self.directory = arena.DATA / 'practice'
        self.ledger = self.directory / 'ledger.jsonl'

    def read(self):
        events = []
        if self.ledger.exists():
            for line in self.ledger.read_text().splitlines():
                event = json.loads(line)
                saved = event.pop('sha256')
                previous = events[-1]['sha256'] if events else '0' * 64
                if event.get('mode') != 'practice' or event['previous'] != previous or hashlib.sha256(self.a.canonical(event).encode()).hexdigest() != saved:
                    raise RuntimeError('Practice ledger integrity failure. Preserve the records.')
                event['sha256'] = saved
                events.append(event)
        return events

    def append(self, events, kind, **fields):
        event = dict(seq=len(events)+1, timestamp=self.a.now(), mode='practice', kind=kind,
                     previous=events[-1]['sha256'] if events else '0'*64, **fields)
        event['sha256'] = hashlib.sha256(self.a.canonical(event).encode()).hexdigest()
        self.directory.mkdir(parents=True, exist_ok=True)
        with self.ledger.open('a') as f:
            f.write(self.a.canonical(event)+'\n'); f.flush(); os.fsync(f.fileno())
        events.append(event)
        return event

    def board(self, game):
        board = self.a.chess.Board(game['start']['initial_fen'])
        for move in game['moves']:
            board.push_uci(move['uci'])
        return board

    def pgn(self, game):
        record = self.a.chess.pgn.Game.from_board(self.board(game))
        start, end = game['start'], game['end']
        record.headers.update(Event='Chess practice — excluded from benchmark Elo', Site='Local',
            Date=start['timestamp'][:10].replace('-', '.'), Round=str(start['game']),
            Result=end['result'] if end else '*', Mode='practice',
            White=self.a.CONFIG['model'] if start['color']=='white' else 'Stockfish 19',
            Black=self.a.CONFIG['model'] if start['color']=='black' else 'Stockfish 19',
            OpponentSetting=start['opponent']['id'], Termination=end['reason'] if end else 'in progress')
        return str(record)+'\n'

    def end(self, events, game, result, reason):
        score = {'1-0':1, '0-1':0, '1/2-1/2':.5, '*':None}[result]
        if score is not None and game['start']['color']=='black': score=1-score
        self.append(events, 'result', game=game['start']['game'], result=result, score=score,
                    reason=reason, plies=len(game['moves']), illegal_attempts=len(game['illegal']))
        ended = self.a.games(events)[-1]
        dest=self.directory/'games'/f"{game['start']['game']:06d}.pgn.gz"
        dest.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(dest,'wt') as f: f.write(self.pgn(ended))

    def adjudicate(self, events, game):
        outcome=self.board(game).outcome(claim_draw=True)
        if outcome:
            self.end(events,game,outcome.result(),outcome.termination.name.lower());return True
        if len(game['moves'])>=self.a.CONFIG['max_plies']:
            self.end(events,game,'*','move_limit_unfinished_not_a_draw');return True
        return False

    def push(self, events, game, move, actor, seconds=None, note=None):
        board=self.board(game);san=board.san(move);board.push(move)
        event=self.append(events,'move',game=game['start']['game'],ply=len(game['moves'])+1,
            actor=actor,uci=move.uci(),san=san,fen=board.fen(),seconds=seconds,note=note)
        game['moves'].append(event)

    def reply(self, events, game):
        if self.adjudicate(events,game):return
        board=self.board(game)
        learner=self.a.chess.WHITE if game['start']['color']=='white' else self.a.chess.BLACK
        if board.turn==learner:return
        started=time.monotonic()
        try:
            with self.a.chess.engine.SimpleEngine.popen_uci(str(self.a.HERE/self.a.CONFIG['engine']),timeout=60) as engine:
                engine.configure(game['start']['opponent']['options'])
                result=engine.play(board,self.a.chess.engine.Limit(nodes=game['start']['nodes_per_move']),info=self.a.chess.engine.INFO_NONE)
            if result.move not in board.legal_moves:raise RuntimeError('Opponent returned an illegal move')
        except Exception as exc:
            self.append(events,'engine_error',game=game['start']['game'],error=str(exc)[:500])
            raise RuntimeError('Practice opponent failed. Recorded position preserved; use practice board to retry.') from exc
        self.push(events,game,result.move,'stockfish',round(time.monotonic()-started,4))
        self.adjudicate(events,game)

    def start(self, events, benchmark, args):
        if self.a.active(benchmark):raise RuntimeError('Finish the active benchmark game before starting practice.')
        if self.a.active(events):raise RuntimeError('Finish or explicitly end the active practice before starting another.')
        options={'Threads':1,'Hash':64}
        if args.elo is not None:
            if not 1320<=args.elo<=3190:raise ValueError('Practice Elo must be between 1320 and 3190 for this pinned engine.')
            options.update(UCI_LimitStrength=True,UCI_Elo=args.elo);name=f'practice-elo-{args.elo}'
        else:
            skill=20 if args.maximum else args.skill
            if skill is None or not 0<=skill<=20:raise ValueError('Practice skill must be between 0 and 20.')
            options.update(UCI_LimitStrength=False,**{'Skill Level':skill});name=f'practice-skill-{skill}'
        source={'kind':'initial'}
        if args.from_game is not None:
            matches=[g for g in self.a.games(benchmark) if g['start']['game']==args.from_game]
            if not matches:raise ValueError('Benchmark source game not found.')
            if args.ply is None or not 0<=args.ply<=len(matches[0]['moves']):raise ValueError('Supply --ply within the recorded source game.')
            board=self.a.chess.Board()
            for event in matches[0]['moves'][:args.ply]:board.push_uci(event['uci'])
            source={'kind':'benchmark','game':args.from_game,'ply':args.ply}
        else:
            if args.ply is not None:raise ValueError('--ply requires --from-game.')
            board=self.a.chess.Board(args.fen) if args.fen else self.a.chess.Board()
            if args.fen:source={'kind':'custom_fen'}
        if not board.is_valid():raise ValueError('Invalid starting chess position.')
        if args.note and len(args.note)>2000:raise ValueError('Practice note limited to 2000 characters.')
        self.append(events,'start',game=len(self.a.games(events))+1,color=args.color,
            opponent={'id':name,'options':options},model=self.a.CONFIG['model'],initial_fen=board.fen(),
            source=source,prior_repetition_history_included=False,nodes_per_move=self.a.CONFIG['nodes_per_move'],
            note=args.note,snapshot=self.a.snapshot(),manifest_sha256=self.a.digest(self.a.HERE/'manifest.json'))
        self.reply(events,self.a.active(events))

    def show(self, events):
        game=self.a.active(events)
        if not game:
            print(json.dumps({'mode':'practice','active_practice':None,
                'last_result':self.a.games(events)[-1]['end'] if self.a.games(events) else None},indent=2));return
        board=self.board(game)
        print(json.dumps({'mode':'practice','excluded_from_elo':True,'practice':game['start']['game'],
            'you':game['start']['color'],'opponent':game['start']['opponent']['id'],
            'fen':board.fen(),'turn':'white' if board.turn else 'black','check':board.is_check(),
            'moves':' '.join(e['san'] for e in game['moves'])},indent=2))
        print('\n'+str(board)+'\n\na b c d e f g h (ranks 8 to 1 from top to bottom)')


def parser():
    p=argparse.ArgumentParser(prog='./play practice',description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    start=sub.add_parser('start')
    strength=start.add_mutually_exclusive_group(required=True)
    strength.add_argument('--elo',type=int);strength.add_argument('--skill',type=int);strength.add_argument('--max',dest='maximum',action='store_true')
    start.add_argument('--color',choices=['white','black'],default='white')
    source=start.add_mutually_exclusive_group()
    source.add_argument('--fen');source.add_argument('--from-game',type=int)
    start.add_argument('--ply',type=int);start.add_argument('--note')
    move=sub.add_parser('move');move.add_argument('uci');move.add_argument('--note')
    for name in ('board','resign','status'):sub.add_parser(name)
    end=sub.add_parser('end');end.add_argument('--note',default='Learner ended practice')
    pgn=sub.add_parser('pgn');pgn.add_argument('--game',type=int)
    return p


def main(argv, arena):
    args=parser().parse_args(argv)
    practice=Practice(arena)
    with (arena.DATA/'.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        arena.verify_install()
        benchmark=arena.read_events();events=practice.read()
        if args.command not in ('status','pgn'):
            if arena.active(benchmark):raise RuntimeError('Finish the active benchmark game before using opponent practice.')
            arena.space_check()
        game=arena.active(events)
        if args.command=='start':practice.start(events,benchmark,args)
        elif args.command=='board':
            if game:practice.reply(events,game)
        elif args.command=='move':
            if not game:raise RuntimeError('No active practice. Use practice start.')
            board=practice.board(game)
            learner=arena.chess.WHITE if game['start']['color']=='white' else arena.chess.BLACK
            if board.turn!=learner:raise RuntimeError('Opponent reply pending; use practice board.')
            if args.note and len(args.note)>2000:raise ValueError('Practice note limited to 2000 characters.')
            try:move=arena.chess.Move.from_uci(args.uci)
            except ValueError:move=None
            if move not in board.legal_moves:
                attempts=1+sum(e['ply']==len(game['moves'])+1 for e in game['illegal'])
                event=practice.append(events,'illegal',game=game['start']['game'],submitted=args.uci[:100],ply=len(game['moves'])+1,attempt=attempts)
                game['illegal'].append(event)
                if attempts>=arena.CONFIG['illegal_attempts_per_turn']:
                    practice.end(events,game,'0-1' if learner else '1-0','illegal_move_forfeit')
                print(json.dumps({'error':'Illegal move','attempt':attempts}))
            else:
                last=game['moves'][-1] if game['moves'] else game['start']
                seconds=(dt.datetime.now(dt.timezone.utc)-dt.datetime.fromisoformat(last['timestamp'])).total_seconds()
                practice.push(events,game,move,'model',round(seconds,4),args.note);practice.reply(events,game)
        elif args.command in ('resign','end'):
            if not game:raise RuntimeError('No active practice.')
            if args.command=='end':
                if len(args.note)>2000:raise ValueError('Practice note limited to 2000 characters.')
                practice.append(events,'note',game=game['start']['game'],text=args.note)
                practice.end(events,game,'*','stopped_by_learner_not_a_result')
            else:practice.end(events,game,'0-1' if game['start']['color']=='white' else '1-0','resignation')
        elif args.command=='pgn':
            games=arena.games(events)
            chosen=next((g for g in games if g['start']['game']==args.game),None) if args.game is not None else (games[-1] if games else None)
            if not chosen:raise ValueError('Practice game not found.')
            print(practice.pgn(chosen));return
        elif args.command=='status':
            games=arena.games(events);ended=[g for g in games if g['end']]
            print(json.dumps({'mode':'practice','excluded_from_elo':True,'started':len(games),
                'active_practice':game['start']['game'] if game else None,
                'completed':sum(g['end']['score'] is not None for g in ended),
                'stopped_or_unfinished':sum(g['end']['score'] is None for g in ended),
                'ledger':str(practice.ledger),'elo_setting_range':[1320,3190],'skill_range':[0,20]},indent=2));return
        practice.show(events)
