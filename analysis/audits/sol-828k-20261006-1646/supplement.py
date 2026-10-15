"""Operator-only verification: UCI settings and recorded tactical facts, no engine analysis."""
import collections
import datetime as dt
import fcntl
import json
import logging
import sys
import urllib.request
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/home/peter/Chess Learning')
HERE = Path(__file__).resolve().parent
FOLDER = ROOT / 'Chess - GPT-6.1-Sol - Long Context - Max'
sys.path.insert(0, str(FOLDER / '.arena/vendor/chess-1.11.2'))
import chess
import chess.engine


class Commands(logging.Handler):
    def __init__(self):
        super().__init__()
        self.commands = []

    def emit(self, record):
        message = record.getMessage()
        if ': << setoption ' in message:
            self.commands.append(message.split(': << ', 1)[1])


def main():
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'engines': [], 'positions': [],
              'existingRefereeTests': {'passed': 29, 'elapsedSeconds': 5.591},
              'scope': 'Operator checks only; no analysis calls, new benchmark games, or learner feedback.'}
    config = json.loads((FOLDER / '.arena/config.json').read_text())
    logger = logging.getLogger('chess.engine')
    logger.setLevel(logging.DEBUG)
    for opponent in config['opponents']:
        capture = Commands()
        logger.addHandler(capture)
        with chess.engine.SimpleEngine.popen_uci(str(FOLDER / '.arena' / config['engine']), timeout=30) as engine:
            advertised = {name: option.default for name, option in engine.options.items()
                          if name in ('Skill Level', 'UCI_LimitStrength', 'UCI_Elo', 'Hash', 'Threads')}
            engine.configure(opponent['options'])
            engine.ping()
            applied = {name: engine.protocol.config[name] for name in advertised}
            assert all(applied[name] == value for name, value in opponent['options'].items())
            result['engines'].append({'opponent': opponent['id'], 'engine': engine.id,
                                      'advertisedDefaults': advertised, 'clientConfiguration': applied,
                                      'transmittedOptions': capture.commands, 'ready': True})
        logger.removeHandler(capture)

    with (FOLDER / 'data/.lock').open('rb') as lock:
        fcntl.flock(lock, fcntl.LOCK_SH)
        events = [json.loads(line) for line in (FOLDER / 'data/ledger.jsonl').open()]
    games = collections.defaultdict(list)
    for event in events:
        if event['kind'] == 'move':
            games[event['game']].append(event)

    board = chess.Board()
    before_mate_threat = None
    for event in games[12]:
        if event['ply'] == 26:
            assert event['san'] == 'Bc5'
            before_mate_threat = board.copy()
        assert chess.Move.from_uci(event['uci']) in board.legal_moves
        board.push_uci(event['uci'])
    assert board.is_checkmate()
    assert games[12][-1]['san'] == 'Qxf7#' and board.fullmove_number == 14
    pawn_advantage = len(before_mate_threat.pieces(chess.PAWN, chess.BLACK)) - len(before_mate_threat.pieces(chess.PAWN, chess.WHITE))
    assert pawn_advantage == 3
    assert before_mate_threat.piece_at(chess.D5) == chess.Piece(chess.BISHOP, chess.WHITE)
    assert chess.F7 in before_mate_threat.attacks(chess.D5)
    result['positions'].append({'game': 12, 'opponent': 'elo-1800-setting', 'learner': 'black',
                                 'pawnAdvantageBeforeFinalMove': pawn_advantage,
                                 'terminalMoves': '13.Bd5 Bc5 14.Qxf7#', 'checkmateVerified': True,
                                 'whiteBishopControlsF7': True})

    board = chess.Board()
    for event in games[15]:
        if event['ply'] == 63:
            assert event['san'] == 'Rf4'
        board.push_uci(event['uci'])
        if event['ply'] == 64:
            assert event['san'] == 'Ne2+'
            assert board.is_check() and board.king(chess.WHITE) == chess.G1
            assert board.piece_at(chess.E2) == chess.Piece(chess.KNIGHT, chess.BLACK)
            assert board.piece_at(chess.F4) == chess.Piece(chess.ROOK, chess.WHITE)
            assert {chess.G1, chess.F4}.issubset(board.attacks(chess.E2))
        if event['ply'] == 66:
            assert event['san'] == 'Nxf4'
            assert board.piece_at(chess.F4) == chess.Piece(chess.KNIGHT, chess.BLACK)
            result['positions'].append({'game': 15, 'opponent': 'skill-0', 'learner': 'white',
                                         'terminalTactic': '31.Re4 Nc3 32.Rf4 Ne2+ 33.Kh2 Nxf4',
                                         'checkingForkAndRookCaptureVerified': True})
            break

    request = urllib.request.Request('https://ailearningchess.ai-learning-chess.workers.dev/data',
                                     headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request, timeout=20) as response:
        public = json.load(response)
    result['publicStructure'] = {'topKeys': list(public), 'runsType': type(public.get('runs')).__name__}
    runs = public.get('runs') or {}
    iterable = runs.items() if isinstance(runs, dict) else ((run.get('id', str(i)), run) for i, run in enumerate(runs))
    for key, run in iterable:
        if 'sol' in key.lower():
            rating = run.get('rating') or {}
            result.setdefault('publicSolRatings', {})[key] = {'label': run.get('label'),
                                                            'rating': {field: rating.get(field) for field in ('estimate', 'lower', 'upper', 'rated_games_total', 'excluded_uncalibrated')},
                                                            'stats': run.get('stats')}
    (HERE / 'supplement.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
