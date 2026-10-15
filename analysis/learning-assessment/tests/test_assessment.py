import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import assess


def recorded(ucis, initial=None):
    board = assess.chess.Board(initial or assess.chess.STARTING_FEN)
    result = {'start': {'game': 1, 'color': 'white'}, 'moves': [], 'illegal': [], 'end': None}
    if initial:
        result['start']['initial_fen'] = initial
    for i, uci in enumerate(ucis):
        move = assess.chess.Move.from_uci(uci)
        san = board.san(move)
        actor = 'model' if board.turn else 'stockfish'
        board.push(move)
        result['moves'].append({'actor': actor, 'uci': uci, 'san': san, 'fen': board.fen(), 'ply': i + 1})
    return result


def rotations(n, score=1):
    blocks = []
    for cycle in range(n):
        group = []
        for i, opponent in enumerate(assess.OPPONENTS):
            for j, color in enumerate(('white', 'black')):
                g = {'start': {'game': cycle * 6 + i * 2 + j + 1, 'opponent': {'id': opponent}, 'color': color},
                     'end': {'score': score}, 'features': {
                         'ownMoves': 10, 'illegal': 0, 'shortLosses': [], 'leadReached': False,
                         'castleBy10': True, 'seconds': [2]}}
                group.append(g)
        blocks.append(group)
    return blocks


class AssessmentTests(unittest.TestCase):
    def test_ledger_tampering_fails_closed(self):
        event = {'kind': 'note', 'seq': 1, 'previous': '0' * 64, 'timestamp': '2026-10-04', 'text': 'original'}
        event['sha256'] = hashlib.sha256(assess.canonical(event).encode()).hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'ledger.jsonl'
            path.write_text(json.dumps(event) + '\n')
            self.assertEqual(assess.read_ledger(path)[1]['events'], 1)
            event['text'] = 'modified'
            path.write_text(json.dumps(event) + '\n')
            with self.assertRaises(ValueError):
                assess.read_ledger(path)

    def test_immediate_piece_loss_detected_after_actual_reply(self):
        game = recorded('e2e4 e7e5 d1h5 b8c6 h5e5 c6e5 g1f3'.split())
        f = assess.replay(game)
        self.assertEqual(len(f['shortLosses']), 1)
        self.assertEqual(f['shortLosses'][0]['piece'], 'Q')
        self.assertEqual(f['shortLosses'][0]['materialChange'], -8)

    def test_equal_exchange_is_not_a_piece_loss_event(self):
        game = recorded('d1d8 e8d8 e1d2'.split(), '3qk3/8/8/8/8/8/8/3QK3 w - - 0 1')
        self.assertEqual(assess.replay(game)['shortLosses'], [])

    def test_missing_next_reply_is_not_scored_as_unrecovered(self):
        game = recorded('e2e4 e7e5 d1h5 b8c6 h5e5 c6e5'.split())
        self.assertEqual(assess.replay(game)['shortLosses'], [])

    def test_wrong_actor_or_fen_rejected(self):
        game = recorded(['e2e4'])
        game['moves'][0]['actor'] = 'stockfish'
        with self.assertRaises(ValueError):
            assess.replay(game)
        game['moves'][0]['actor'] = 'model'
        game['moves'][0]['fen'] = assess.chess.STARTING_FEN
        with self.assertRaises(ValueError):
            assess.replay(game)

    def test_primary_windows_disjoint_and_balanced(self):
        games = [g for block in rotations(11) for g in block]
        t = assess.trends(games)['primary']
        self.assertFalse(set(t['earlyGames']) & set(t['lateGames']))
        self.assertEqual(t['early']['games'], 20)
        self.assertEqual(t['late']['games'], 20)
        for counts in t['byOpponent'].values():
            self.assertEqual(counts['early']['games'], counts['late']['games'])

    def test_incomplete_rotation_excluded_from_primary(self):
        games = [g for block in rotations(3) for g in block][:-1]
        self.assertEqual(len(assess.complete_rotations(games)), 2)
        self.assertEqual(assess.trends(games)['primary']['status'], 'Too few games')

    def test_block_resampling_and_full_strength_separation(self):
        a, b = rotations(5, 0), rotations(5, 1)
        for block in b:
            for g in block[:2]:
                g['end']['score'] = 0
        result = assess.compare_blocks(a, b)
        self.assertEqual(result['delta'], 1)
        self.assertEqual(result['interval'], [1, 1])
        self.assertEqual(result['status'], 'Improved in matched windows')
        self.assertEqual(result['byOpponent']['full-strength']['late']['score'], 0)

    def test_stopped_practice_does_not_count_as_draw(self):
        games = [{'end': {'score': None}}, {'end': {'score': .5}}, {'end': None}]
        result = assess.tally(games)
        self.assertEqual((result['games'], result['draws']), (1, 1))


if __name__ == '__main__':
    unittest.main()
