#!/usr/bin/env python3
"""Small, event-sourced chess referee. No analysis API or move recommendations."""
import argparse
import contextlib
import datetime as dt
import fcntl
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import sys
import tarfile
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE / 'vendor/chess-1.11.2'))
import chess
import chess.engine
import chess.pgn

DATA = ROOT / 'data'
WORK = ROOT / 'workspace'
LEDGER = DATA / 'ledger.jsonl'
CONFIG = json.loads((HERE / 'config.json').read_text())
EXPORT = ROOT.parent / 'deliverables'

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def digest(p):
    with p.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False)

def read_events():
    events = []
    if LEDGER.exists():
        with LEDGER.open() as f:
            for line in f:
                event = json.loads(line)
                saved = event.pop('sha256')
                previous = events[-1]['sha256'] if events else '0' * 64
                if event['previous'] != previous or hashlib.sha256(canonical(event).encode()).hexdigest() != saved:
                    raise RuntimeError('Ledger integrity failure. Preserve files; do not reset history.')
                event['sha256'] = saved
                events.append(event)
    return events

def append(events, kind, **fields):
    event = dict(seq=len(events) + 1, timestamp=now(), kind=kind,
                 previous=events[-1]['sha256'] if events else '0' * 64, **fields)
    event['sha256'] = hashlib.sha256(canonical(event).encode()).hexdigest()
    with LEDGER.open('a') as f:
        f.write(canonical(event) + '\n')
        f.flush()
        os.fsync(f.fileno())
    events.append(event)
    return event

def size(path):
    return sum(p.stat().st_size for p in path.rglob('*') if p.is_file() and not p.is_symlink())

def space_check():
    if size(DATA) + size(WORK) >= CONFIG['storage_limit_bytes']:
        raise RuntimeError('Recording/workspace storage limit reached. History preserved; ask operator to archive or expand storage.')
    if shutil.disk_usage(ROOT).free < 2 * 1024**3:
        raise RuntimeError('Less than 2 GiB disk free. Paused without deleting records.')

def snapshot():
    files = sorted(p for p in WORK.rglob('*') if p.is_file())
    if any(p.is_symlink() or WORK.resolve() not in p.resolve().parents for p in files):
        raise RuntimeError('Workspace snapshots cannot follow symlinks outside the workspace.')
    if sum(p.stat().st_size for p in files) > 32 * 1024**2:
        raise RuntimeError('Workspace exceeds 32 MiB snapshot limit; preserve large material outside this experiment or ask operator.')
    listing = {str(p.relative_to(WORK)): digest(p) for p in files}
    key = hashlib.sha256(canonical(listing).encode()).hexdigest()
    dest = DATA / 'snapshots' / (key + '.tar.gz')
    dest.parent.mkdir(exist_ok=True)
    if not dest.exists():
        tmp = dest.with_suffix('.tmp')
        with tarfile.open(tmp, 'w:gz') as archive:
            for p in files:
                archive.add(p, arcname=str(p.relative_to(WORK)), recursive=False)
        tmp.replace(dest)
    return key

def games(events):
    result = {}
    for e in events:
        if e['kind'] == 'start':
            result[e['game']] = dict(start=e, moves=[], illegal=[], end=None)
        elif e.get('game') in result:
            g = result[e['game']]
            if e['kind'] == 'move': g['moves'].append(e)
            elif e['kind'] == 'illegal': g['illegal'].append(e)
            elif e['kind'] == 'result': g['end'] = e
    return list(result.values())

def active(events):
    gs = games(events)
    return gs[-1] if gs and not gs[-1]['end'] else None

def board_for(g):
    b = chess.Board()
    for e in g['moves']: b.push_uci(e['uci'])
    return b

def pgn_for(g):
    b = board_for(g)
    game = chess.pgn.Game.from_board(b)
    start = g['start']
    end = g['end']
    game.headers.update(Event='Chess Learning v1', Site='Local', Date=start['timestamp'][:10].replace('-', '.'),
                        Round=str(start['game']), Result=end['result'] if end else '*')
    game.headers['White'] = CONFIG['model'] if start['color'] == 'white' else 'Stockfish 19'
    game.headers['Black'] = CONFIG['model'] if start['color'] == 'black' else 'Stockfish 19'
    game.headers['OpponentSetting'] = start['opponent']['id']
    game.headers['Termination'] = end['reason'] if end else 'in progress'
    game.headers['WorkspaceSnapshot'] = start['snapshot']
    return str(game) + '\n'

def end_game(events, g, result, reason):
    white_score = {'1-0': 1, '0-1': 0, '1/2-1/2': .5, '*': None}[result]
    score = white_score if g['start']['color'] == 'white' or white_score is None else 1 - white_score
    append(events, 'result', game=g['start']['game'], result=result, score=score, reason=reason,
           plies=len(g['moves']), illegal_attempts=len(g['illegal']), snapshot=snapshot())
    refreshed = games(events)[-1]
    path = DATA / 'games' / f"{g['start']['game']:06d}.pgn.gz"
    path.parent.mkdir(exist_ok=True)
    with gzip.open(path, 'wt') as f: f.write(pgn_for(refreshed))

def adjudicate(events, g):
    b = board_for(g)
    outcome = b.outcome(claim_draw=True)
    if outcome:
        end_game(events, g, outcome.result(), outcome.termination.name.lower())
        return True
    if len(g['moves']) >= CONFIG['max_plies']:
        end_game(events, g, '*', 'move_limit_unfinished_not_a_draw')
        return True
    return False

def push(events, g, move, actor, note=None, seconds=None, tokens=None):
    b = board_for(g)
    san = b.san(move)
    b.push(move)
    e = append(events, 'move', game=g['start']['game'], actor=actor,
               ply=len(g['moves']) + 1, uci=move.uci(), san=san, fen=b.fen(),
               seconds=seconds, reported_tokens=tokens, note=note)
    g['moves'].append(e)

def engine_reply(events, g):
    if adjudicate(events, g): return
    b = board_for(g)
    learner = chess.WHITE if g['start']['color'] == 'white' else chess.BLACK
    if b.turn == learner: return
    started = time.monotonic()
    try:
        with chess.engine.SimpleEngine.popen_uci(str(HERE / CONFIG['engine']), timeout=60) as engine:
            engine.configure(g['start']['opponent']['options'])
            reply = engine.play(b, chess.engine.Limit(nodes=CONFIG['nodes_per_move']), info=chess.engine.INFO_NONE)
        if reply.move not in b.legal_moves: raise RuntimeError('Engine returned an illegal move')
    except Exception as e:
        append(events, 'engine_error', game=g['start']['game'], error=str(e)[:500])
        raise RuntimeError('Opponent failed. Game preserved; use board to retry its pending turn.') from e
    push(events, g, reply.move, 'stockfish', seconds=round(time.monotonic() - started, 4))
    adjudicate(events, g)

def show(events):
    g = active(events)
    if not g:
        print(json.dumps({'active_game': None, 'last_result': games(events)[-1]['end'] if games(events) else None}, indent=2))
        return
    b = board_for(g)
    print(json.dumps({'game': g['start']['game'], 'you': g['start']['color'],
                      'opponent': g['start']['opponent']['id'], 'fen': b.fen(),
                      'turn': 'white' if b.turn else 'black', 'check': b.is_check(),
                      'moves': ' '.join(e['san'] for e in g['moves'])}, indent=2))
    print('\n' + str(b) + '\n\na b c d e f g h (ranks 8 to 1 from top to bottom)')

def statistics(gs):
    result = []
    for opponent in CONFIG['opponents']:
        selected = [g for g in gs if g['start']['opponent']['id'] == opponent['id']]
        ended = [g for g in selected if g['end'] and g['end']['score'] is not None]
        scores = [g['end']['score'] for g in ended]
        rolling = scores[-50:]
        result.append(dict(opponent=opponent['id'], started=len(selected), completed=len(ended),
                           wins=scores.count(1), draws=scores.count(.5), losses=scores.count(0),
                           unfinished=sum(bool(g['end']) and g['end']['score'] is None for g in selected),
                           score=sum(scores)/len(scores) if scores else None,
                           rolling_score=sum(rolling)/len(rolling) if rolling else None))
    return result

def dashboard(events, dest=None):
    gs = games(events)
    payload = dict(generated=now(), model=CONFIG['model'], stats=statistics(gs),
                   usage=[e for e in events if e['kind'] == 'usage'][-100:],
                   notes=[e for e in events if e['kind'] == 'note'][-50:],
                   settings=CONFIG, events=len(events), bytes=size(DATA)+size(WORK),
                   ledger_head=events[-1]['sha256'] if events else None, games=[])
    for g in gs[-100:]:
        payload['games'].append(dict(id=g['start']['game'], start=g['start'], end=g['end'],
                                     moves=g['moves'], illegal=g['illegal'], pgn=pgn_for(g)))
    template = (HERE / 'viewer.html').read_text()
    text = template.replace('__PAYLOAD__', canonical(payload).replace('<', '\\u003c'))
    target = dest or DATA / 'dashboard.html'
    target.write_text(text)
    return target

def verify_install():
    manifest = json.loads((HERE / 'manifest.json').read_text())
    for rel, expected in manifest.items():
        if digest(ROOT / rel) != expected:
            raise RuntimeError(f'Pinned installation changed: {rel}. Operator review required; learner must not repair or repin.')

def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    for name in ['start', 'board', 'resign', 'status', 'export', 'verify']:
        sub.add_parser(name)
    move = sub.add_parser('move'); move.add_argument('uci'); move.add_argument('--note'); move.add_argument('--tokens', type=int)
    note = sub.add_parser('note'); note.add_argument('text')
    usage = sub.add_parser('usage'); usage.add_argument('--total-tokens', type=int, required=True); usage.add_argument('--source', required=True)
    args = p.parse_args()
    DATA.mkdir(exist_ok=True); WORK.mkdir(exist_ok=True)
    with (DATA / '.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        verify_install()
        events = read_events()
        if args.command in ['start', 'board', 'move', 'resign', 'note', 'usage']:
            space_check()
        if args.command == 'start':
            if active(events): raise RuntimeError('Finish the active game first; results cannot be discarded.')
            n = len(games(events))
            opponent = CONFIG['opponents'][(n // 2) % len(CONFIG['opponents'])]
            append(events, 'start', game=n+1, color='white' if n % 2 == 0 else 'black',
                   opponent=opponent, model=CONFIG['model'], snapshot=snapshot(),
                   protocol=CONFIG['protocol'], nodes_per_move=CONFIG['nodes_per_move'],
                   manifest_sha256=digest(HERE / 'manifest.json'))
            engine_reply(events, active(events)); show(events)
        elif args.command == 'board':
            if active(events): engine_reply(events, active(events))
            show(events)
        elif args.command == 'move':
            g = active(events)
            if not g: raise RuntimeError('No active game; use start.')
            b = board_for(g)
            learner = chess.WHITE if g['start']['color'] == 'white' else chess.BLACK
            if b.turn != learner: raise RuntimeError('Opponent reply pending; use board to resume.')
            if args.tokens is not None and args.tokens < 0: raise RuntimeError('Tokens cannot be negative.')
            if args.note and len(args.note) > 2000: raise RuntimeError('Move comment limited to 2000 characters.')
            try: move = chess.Move.from_uci(args.uci)
            except ValueError: move = None
            if move not in b.legal_moves:
                attempts = 1 + sum(e['ply'] == len(g['moves'])+1 for e in g['illegal'])
                e = append(events, 'illegal', game=g['start']['game'], submitted=args.uci[:100], ply=len(g['moves'])+1, attempt=attempts)
                g['illegal'].append(e)
                if attempts >= CONFIG['illegal_attempts_per_turn']:
                    end_game(events, g, '0-1' if learner else '1-0', 'illegal_move_forfeit')
                print(json.dumps({'error':'Illegal move', 'attempt':attempts}))
            else:
                last = g['moves'][-1] if g['moves'] else g['start']
                seconds = (dt.datetime.now(dt.timezone.utc)-dt.datetime.fromisoformat(last['timestamp'])).total_seconds()
                push(events, g, move, 'model', note=args.note, seconds=round(seconds, 4), tokens=args.tokens)
                engine_reply(events, g)
            show(events)
        elif args.command == 'resign':
            g = active(events)
            if not g: raise RuntimeError('No active game.')
            end_game(events, g, '0-1' if g['start']['color']=='white' else '1-0', 'resignation')
            show(events)
        elif args.command == 'note':
            if len(args.text)>8000: raise RuntimeError('Activity notes limited to 8000 characters.')
            append(events, 'note', text=args.text, snapshot=snapshot())
        elif args.command == 'usage':
            if args.total_tokens<0: raise RuntimeError('Tokens cannot be negative.')
            append(events, 'usage', cumulative_tokens=args.total_tokens, source=args.source[:200], scope='source counter; not per-move attribution')
        elif args.command == 'status':
            print(json.dumps(dict(stats=statistics(games(events)), active_game=active(events)['start']['game'] if active(events) else None,
                                  storage_bytes=size(DATA)+size(WORK), elo=None,
                                  elo_note='Uncalibrated: opponent strength labels are not measured human Elo.'), indent=2))
        elif args.command == 'verify':
            print(json.dumps({'installation':'verified','ledger_events':len(events),'ledger':'hash chain verified'}))
        if args.command == 'export':
            EXPORT.mkdir(exist_ok=True)
            stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d-%H%M%S-%f')
            print(dashboard(events, EXPORT / f'chess-gpt6-astra-{stamp}.html'))
        else: dashboard(events)

if __name__ == '__main__':
    try: main()
    except (RuntimeError, ValueError) as e:
        print(json.dumps({'error':str(e)}), file=sys.stderr)
        sys.exit(1)
