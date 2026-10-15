"""Between-game legality of explicitly supplied remembered lines only.

No search, scoring, candidate generation, attack maps, or engine calls.
"""
import gzip
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.arena/vendor/chess-1.11.2'))
import chess
import chess.pgn

CASES = [
    (185, 70, [('actual promoted queen loss', ['e8e4', 'd5e4']),
               ('chosen supported queen line', ['e8e7', 'a1e5', 'e7e5'])]),
    (186, 47, [('actual rook loss', ['e6d5', 'e4e8']),
               ('original repair with missed bishop blocker', ['e8d8', 'e4e8', 'd8e8']),
               ('corrected supplied continuation', ['e8d8', 'c1b2', 'd7d3'])]),
    (184, 37, [('actual boxed rook', ['d5e4', 'c1d2', 'e3d3', 'f1d3', 'e4d3', 'd2d3']),
               ('chosen rook recapture and retreat', ['e3e4', 'f1d3', 'e4e8'])]),
]

out = []
for number, ply, lines in CASES:
    with gzip.open(ROOT / f'data/games/{number:06d}.pgn.gz', 'rt') as stream:
        game = chess.pgn.read_game(stream)
    position = game.board()
    for index, move in enumerate(game.mainline_moves()):
        if index == ply:
            break
        position.push(move)
    item = {'game': number, 'ply': ply, 'fen': position.fen(), 'lines': []}
    for label, ucis in lines:
        board = position.copy()
        results = []
        for uci in ucis:
            move = chess.Move.from_uci(uci)
            legal = board.is_legal(move)
            result = {'uci': uci, 'legal': legal}
            if legal:
                result['san'] = board.san(move)
                board.push(move)
            results.append(result)
            if not legal:
                break
        item['lines'].append({'label': label, 'moves': results, 'final_fen': board.fen()})
    out.append(item)
report = json.dumps(out, indent=2)
(ROOT / 'workspace/trials/actual-defenders-27-legality.json').write_text(report + '\n')
print(report)
