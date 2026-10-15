"""Between-game reconstruction and legality of supplied lines only; no analysis."""
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
    (191, 52, [('actual king abandons knight', ['c4d5', 'c2c3']),
               ('chosen king retains knight support', ['c4d4', 'c2c1', 'c3e4'])]),
    (188, 43, [('actual double rook fork', ['e8f8', 'b6d7', 'b8c8', 'd7f8', 'd8f8']),
               ('chosen rook avoids f8 fork square', ['e8e7', 'b6d7', 'b8c8'])]),
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
(ROOT / 'workspace/trials/retain-defender-28-legality.json').write_text(report + '\n')
print(report)
