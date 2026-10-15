"""Between-game mechanical reconstruction of explicitly supplied remembered lines.

No move generation, search, scoring, attack maps, or engine calls.
"""
import gzip
import io
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.arena/vendor/chess-1.11.2'))
import chess
import chess.pgn

CASES = [
 (176, 65, [('actual queen loss', ['c8c6','d5c6']), ('chosen retreat line', ['c8d8','c6c7','d8d7'])]),
 (179, 64, [('actual checking fork', ['d5d4','f4e3','g1h1','e3d4','f3d4']), ('chosen quiet line', ['h3h4','f4e3','g1h1'])]),
 (180, 41, [('actual queen fork', ['d6e5','c2c7','a5a8','c7d7']), ('chosen retreat line', ['f6e7','e5d6','e7d6'])]),
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
(ROOT / 'workspace/trials/first-reply-26-legality.json').write_text(report + '\n')
print(report)
