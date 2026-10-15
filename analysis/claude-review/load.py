import json, sys, collections, statistics, datetime as dt, gzip, tarfile, hashlib
from pathlib import Path
ROOT = Path('/home/peter/Chess Learning')
sys.path.insert(0, str(ROOT / 'Chess - GPT-6-Astra/.arena/vendor/chess-1.11.2'))
import chess
RUNS = {
    'astra': 'Chess - GPT-6-Astra',
    'opus': 'Chess - Opus-5.5',
    'sol': 'Chess - GPT-6.1-Sol',
    'solLC': 'Chess - GPT-6.1-Sol - Long Context',
    'fable': 'Chess - Fable-5.1',
}
VAL = {chess.PAWN:1, chess.KNIGHT:3, chess.BISHOP:3, chess.ROOK:5, chess.QUEEN:9, chess.KING:0}
def ts(s): return dt.datetime.fromisoformat(s)
def ledger(path):
    if not path.exists(): return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
def games_of(events):
    g = collections.OrderedDict(); other=[]
    for e in events:
        k = e['kind']; n = e.get('game')
        if k == 'start': g[n] = {'start': e, 'moves': [], 'illegal': [], 'end': None, 'notes': []}
        elif n in g and k == 'move': g[n]['moves'].append(e)
        elif n in g and k == 'illegal': g[n]['illegal'].append(e)
        elif n in g and k == 'result': g[n]['end'] = e
        else: other.append(e)
    return g, other
def mat(board, color):
    return sum(v*(len(board.pieces(p,color))-len(board.pieces(p,not color))) for p,v in VAL.items())
def load(key):
    folder = ROOT / RUNS[key]
    ev = ledger(folder/'data/ledger.jsonl')
    g, other = games_of(ev)
    pev = ledger(folder/'data/practice/ledger.jsonl')
    pg, pother = games_of(pev)
    return folder, ev, g, other, pev, pg, pother
