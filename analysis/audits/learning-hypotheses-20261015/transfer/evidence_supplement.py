#!/usr/bin/env python3
"""Describe recorded illegal requests and pin small authored evidence files.

No engines, new move decisions, or private model reasoning are used.
"""
import collections
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('transfer', HERE / 'assess_transfer.py')
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
chess = t.a.chess


def illegal_reason(board, submitted):
    try:
        move = chess.Move.from_uci(submitted)
    except ValueError:
        return {'kind': 'unparsed-UCI', 'submitted': submitted}
    piece = board.piece_at(move.from_square)
    if not piece:
        return {'kind': 'empty-origin'}
    if piece.color != board.turn:
        return {'kind': 'wrong-side-origin'}
    target = board.piece_at(move.to_square)
    if target and target.color == piece.color:
        return {'kind': 'friendly-occupied-destination'}
    if board.is_pseudo_legal(move):
        assert not board.is_legal(move)
        return {'kind': 'king-safety', 'alreadyInCheck': board.is_check()}
    if piece.piece_type in (chess.BISHOP, chess.ROOK, chess.QUEEN):
        blockers = chess.between(move.from_square, move.to_square) & board.occupied
        if blockers:
            return {'kind': 'blocked-slider-path',
                    'blockers': {chess.square_name(s): board.piece_at(s).symbol() for s in chess.scan_forward(blockers)}}
    if piece.piece_type == chess.PAWN:
        dy = chess.square_rank(move.to_square) - chess.square_rank(move.from_square)
        if (piece.color == chess.WHITE and dy <= 0) or (piece.color == chess.BLACK and dy >= 0):
            return {'kind': 'backward-or-horizontal-pawn'}
        return {'kind': 'other-pawn-geometry'}
    return {'kind': 'other-piece-geometry-or-rule'}


def analyze_illegals(manifest, slug):
    info = manifest['runs'][t.selected_run(manifest, slug)]['files']['data/ledger.jsonl']
    p = Path(info['snapshot'])
    assert t.digest_bytes(p.read_bytes()) == info['sha256']
    events, _ = t.a.read_ledger(p)
    boards, examples = {}, []
    for event in events:
        number = event.get('game')
        if event['kind'] == 'start':
            boards[number] = chess.Board(event.get('initial_fen', chess.STARTING_FEN))
        elif event['kind'] == 'move':
            boards[number].push_uci(event['uci'])
        elif event['kind'] == 'illegal':
            board = boards[number]
            assert event['ply'] == len(board.move_stack) + 1
            examples.append({'game': number, 'ply': event['ply'], 'submitted': event['submitted'],
                             'fen': board.fen(), **illegal_reason(board, event['submitted'])})
    result = json.loads((HERE / f'{slug}.json').read_text())
    early = set(result['matchedHalves']['early']['gameNumbers'])
    late = set(result['matchedHalves']['late']['gameNumbers'])
    return {'all': dict(collections.Counter(e['kind'] for e in examples)),
            'matchedEarly': dict(collections.Counter(e['kind'] for e in examples if e['game'] in early)),
            'matchedLate': dict(collections.Counter(e['kind'] for e in examples if e['game'] in late)),
            'examples': examples}


def recorded_lines(manifest, slug, games_wanted, terminal_plies=8):
    games, _ = t.read_games(manifest, slug, 'data/ledger.jsonl')
    output = []
    for g in games:
        if g['start']['game'] not in games_wanted:
            continue
        output.append({'game': g['start']['game'], 'end': g['end'],
                       'terminalMoves': [{k: e[k] for k in ['ply', 'actor', 'san', 'uci', 'fen']}
                                         for e in g['moves'][-terminal_plies:]],
                       'shortLosses': g['features']['shortLosses']})
    return output


def pin_authored(slug, relative_paths):
    folder = t.ROOT / t.CONFIG[slug][0]
    result = []
    for relative in relative_paths:
        source = folder / 'workspace' / relative
        value = source.read_bytes()
        saved = HERE / 'authored-final-copies' / slug / relative
        saved.parent.mkdir(parents=True, exist_ok=True)
        saved.write_bytes(value)
        assert source.read_bytes() == value
        result.append({'source': str(source), 'sha256': t.digest_bytes(value), 'copy': str(saved),
                       'provenance': 'Final authored file copied read-only; claims distinguished from mechanical replay.'})
    return result


def main():
    manifest = json.loads((t.SNAPS / 'manifest.json').read_text())
    result = {'method': __doc__, 'illegalTypes': {}, 'selectedRecordedGames': {}, 'authoredSources': {}}
    for slug in ['astra', 'sol', 'sol-long', 'sol-long-max']:
        result['illegalTypes'][slug] = analyze_illegals(manifest, slug)
    wanted = {'astra': [173, 197, 198, 199, 200], 'sol': [145, 146, 147, 197, 198, 199, 200],
              'sol-long': [94, 95, 96, 99], 'sol-long-max': [60, 61, 62, 63]}
    for slug, numbers in wanted.items():
        result['selectedRecordedGames'][slug] = recorded_lines(manifest, slug, numbers)
    result['authoredSources']['astra'] = pin_authored('astra', ['final-report-200.md', 'trials/rook-finish-21.md',
                                                             'trials/retain-defender-28.md', 'trials/complete-position-29.md'])
    result['authoredSources']['sol'] = pin_authored('sol', [f'review{i}.md' for i in [145, 146, 147, 197, 198, 199, 200]])
    t.dump(HERE / 'supplement.json', result)
    for slug, values in result['illegalTypes'].items():
        print(slug, values['all'])


if __name__ == '__main__':
    main()
