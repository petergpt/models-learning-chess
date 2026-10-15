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
    (173, 80, [
        ('failed backward recapture', ['e3g3', 'g4g3', 'h4g3']),
        ('one chosen alternative', ['e3f3', 'g4g6', 'd6e4']),
    ]),
    (173, 112, [
        ('failed rook path', ['h2h7']),
        ('one chosen escape line', ['h6g5', 'h7g7', 'g5h4']),
    ]),
    (172, 35, [
        ('failed bishop geometry', ['f7f5']),
        ('actual legal alternative', ['d7f5', 'c2c7', 'f5d7']),
    ]),
    (174, 71, [
        ('actual exchange sequence', ['f6h7', 'e7h7', 'h6h7', 'g5h7', 'h4h7']),
    ]),
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
(ROOT / 'workspace/trials/literal-recaptures-25-legality.json').write_text(report + '\n')
print(report)
