#!/usr/bin/env python3
"""Review helper: print the recorded FEN + rendered board after given plies of a benchmark or practice game.
Reads the referee's own ledger records (read-only). Mechanical rendering only: no search, scoring or move suggestions.
Usage: gamepos.py [--practice] GAME [PLY ...]   (no PLY -> print the SAN move list with ply numbers)"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fen2board import render

ROOT = Path(__file__).resolve().parents[2]
args = sys.argv[1:]
practice = False
if args and args[0] == '--practice':
    practice = True; args = args[1:]
game = int(args[0]); plies = [int(x) for x in args[1:]]
ledger = ROOT / 'data' / ('practice/ledger.jsonl' if practice else 'ledger.jsonl')
moves, start = [], None
for line in ledger.read_text().splitlines():
    e = json.loads(line)
    if e.get('game') != game: continue
    if e['kind'] == 'start': start = e
    elif e['kind'] == 'move': moves.append(e)
if start is None: sys.exit('game not found')
init = start.get('initial_fen', 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
if not plies:
    print(f"game {game} you={start['color']} opp={start['opponent']['id']}")
    line = []
    for m in moves:
        line.append(f"{m['ply']}:{m['san']}")
    print(' '.join(line))
    sys.exit()
for p in plies:
    fen = init if p == 0 else moves[p-1]['fen']
    last = moves[p-1]['san'] if p else '-'
    print(f"after ply {p} (last {last}):")
    print(fen)
    print(render(fen))
    print()
