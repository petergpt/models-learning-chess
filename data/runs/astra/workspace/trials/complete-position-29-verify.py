"""Remembered positions only: verify supplied moves, without move selection."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import gzip
import io
import json

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.arena/vendor/chess-1.11.2'))
import chess
import chess.pgn

cases = [
    (198, 33, 'played', ['e6f5', 'c2f5']),
    (198, 33, 'chosen alternative', ['e6f7', 'b4b5', 'a6b5']),
    (197, 90, 'played', ['c7c8q']),
    (197, 90, 'chosen alternative',
     ['d6e7', 'h7h8', 'c7c8q', 'h8h7', 'c8h3', 'h7g8',
      'e7d8', 'g8f8', 'h3h8']),
]
rows = []
for number, ply, label, supplied in cases:
    with gzip.open(ROOT / f'data/games/{number:06}.pgn.gz', 'rt') as f:
        game = chess.pgn.read_game(io.StringIO(f.read()))
    board = game.board()
    for i, move in enumerate(game.mainline_moves()):
        if i >= ply:
            break
        board.push(move)
    row = {'game': number, 'ply': ply, 'label': label,
           'start_fen': board.fen(), 'start_board': str(board), 'moves': []}
    for uci in supplied:
        move = chess.Move.from_uci(uci)
        legal = board.is_legal(move)
        row['moves'].append({'uci': uci, 'legal': legal})
        if not legal:
            break
        board.push(move)
    row['end_fen'] = board.fen()
    row['end_board'] = str(board)
    rows.append(row)
output = ROOT / 'workspace/trials/complete-position-29-legality.json'
output.write_text(json.dumps(rows, indent=2) + '\n')
print(json.dumps(rows, indent=2))
