"""Operator-only retrospective resignation audit; never supplies moves to a learner."""
import datetime as dt
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/home/peter/Chess Learning')
HERE = Path(__file__).resolve().parent
ENGINE_FOLDER = ROOT / 'Chess - GPT-6.1-Sol - Long Context - Max/.arena'
sys.path.insert(0, str(ENGINE_FOLDER / 'vendor/chess-1.11.2'))
import chess
import chess.engine


def main():
    audit = json.loads((HERE / 'audit.json').read_text())
    config = json.loads((ENGINE_FOLDER / 'config.json').read_text())
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'nodesPerPosition': 1000000,
              'method': 'Retrospective full-strength Stockfish 19 static endpoint assessment, fresh process per position; no move recommendations exported.',
              'limitation': 'Finite search evaluation is not proof of a forced result, and does not estimate weakened Stockfish conversion probability.',
              'runs': {}}
    for key in ('medium', 'max', 'standard-max'):
        rows = []
        for game in audit['runs'][key]['matchedGames']:
            if game['reason'] != 'resignation' or game['opponent'] == 'full-strength':
                continue
            board = chess.Board(game['fen'])
            learner = chess.WHITE if game['color'] == 'white' else chess.BLACK
            with chess.engine.SimpleEngine.popen_uci(str(ENGINE_FOLDER / config['engine']), timeout=30) as engine:
                engine.configure({'Threads': 1, 'Hash': 64, 'Skill Level': 20, 'UCI_LimitStrength': False})
                info = engine.analyse(board, chess.engine.Limit(nodes=1000000), info=chess.engine.INFO_SCORE)
            score = info['score'].pov(learner)
            row = {'game': game['game'], 'opponent': game['opponent'], 'learner': game['color'],
                   'scoreCentipawns': score.score(), 'mate': score.mate()}
            rows.append(row)
            print(json.dumps({'run': key, **row}), flush=True)
        result['runs'][key] = rows
    (HERE / 'resignations.json').write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
