"""Post-hoc move-quality review of benchmark games (operator analysis only).
Evaluates every position once with Stockfish 19 at fixed nodes; caches per game."""
import sys, json, os, math
from pathlib import Path
from multiprocessing import Pool
sys.path.insert(0, '/home/peter/Chess Learning/Chess - GPT-6-Astra/.arena/vendor/chess-1.11.2')
sys.path.insert(0, '/home/peter/Chess Learning/.operator/claude-review')
import chess, chess.engine
from load import RUNS, load
NODES = 200000
OUT = Path('/home/peter/Chess Learning/.operator/claude-review/evals')
_eng = None
def eng():
    global _eng
    if _eng is None:
        _eng = chess.engine.SimpleEngine.popen_uci('/home/peter/Chess Learning/Chess - GPT-6-Astra/.arena/stockfish/stockfish/stockfish-linux-x86-64-universal')
        _eng.configure({'Threads': 1, 'Hash': 64})
    return _eng
def score_cp(info, turn):
    s = info['score'].pov(turn)
    if s.is_mate():
        m = s.mate()
        return 10000 - abs(m) * 10 if m > 0 else -(10000 - abs(m) * 10)
    return s.score()
def analyse_game(task):
    key, gnum, start_fen, ucis, learner_white = task
    path = OUT / f'{key}-{gnum:03d}.json'
    if path.exists():
        return str(path)
    e = eng()
    e.configure({'Clear Hash': None}) if False else None
    board = chess.Board(start_fen)
    evals = []   # eval of each position from side-to-move perspective, plus best move
    for i in range(len(ucis) + 1):
        if board.is_game_over(claim_draw=False):
            o = board.outcome()
            if o.winner is None: evals.append((0, None))
            else: evals.append((-10000 if o.winner != board.turn else 10000, None))
        else:
            info = e.analyse(board, chess.engine.Limit(nodes=NODES))
            pv = info.get('pv') or [None]
            evals.append((score_cp(info, board.turn), pv[0].uci() if pv[0] else None))
        if i < len(ucis):
            board.push_uci(ucis[i])
    moves = []
    board = chess.Board(start_fen)
    for i, u in enumerate(ucis):
        mover_white = board.turn == chess.WHITE
        actor = 'model' if mover_white == learner_white else 'sf'
        before = evals[i][0]            # mover's perspective
        after = -evals[i + 1][0]        # mover's perspective after move
        moves.append({'ply': i + 1, 'actor': actor, 'uci': u, 'san': board.san(chess.Move.from_uci(u)),
                      'before': before, 'after': after, 'best': evals[i][1]})
        board.push_uci(u)
    path.write_text(json.dumps({'run': key, 'game': gnum, 'learnerWhite': learner_white, 'moves': moves}))
    return str(path)
def tasks():
    out = []
    for key in RUNS:
        folder, ev, g, other, pev, pg, pother = load(key)
        for n, x in g.items():
            if not x['end'] or x['end']['score'] is None: continue
            out.append((key, n, x['start'].get('initial_fen', chess.STARTING_FEN),
                        [m['uci'] for m in x['moves']], x['start']['color'] == 'white'))
    # longest first for load balance
    out.sort(key=lambda t: -len(t[3]))
    return out
if __name__ == '__main__':
    T = [t for t in tasks() if not (OUT / f'{t[0]}-{t[1]:03d}.json').exists()]
    print('games to analyse', len(T), 'positions', sum(len(t[3]) + 1 for t in T), flush=True)
    with Pool(int(sys.argv[1]) if len(sys.argv) > 1 else 8) as p:
        for i, r in enumerate(p.imap_unordered(analyse_game, T)):
            if i % 25 == 0: print(i, r, flush=True)
    print('done', flush=True)
