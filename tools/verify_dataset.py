#!/usr/bin/env python3
"""Verify exported chains, workspace archives, moves, PGNs, and trace structure."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import sys
import tarfile

ROOT = Path(__file__).resolve().parent.parent


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def rows(path):
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt', encoding='utf-8') as stream:
        for line in stream:
            if line.strip():
                yield json.loads(line)


def check_manifest(root):
    manifest = json.loads((root / 'manifest.json').read_text())
    excluded = {'.git', '.cache', '__pycache__', '.venv', 'node_modules'}
    expected = {p.relative_to(root).as_posix() for p in root.rglob('*')
                if p.is_file() and not p.is_symlink() and p != root / 'manifest.json'
                and p.relative_to(root).parts[0] != 'runs'
                and not any(part in excluded for part in p.relative_to(root).parts)}
    assert expected == set(manifest['files']), 'Release manifest does not cover every distributable file.'
    for name, record in manifest['files'].items():
        path = root / name
        assert path.is_file() and not path.is_symlink(), 'Missing release file: ' + name
        with path.open('rb') as stream:
            actual = hashlib.file_digest(stream, 'sha256').hexdigest()
        assert actual == record['sha256'] and path.stat().st_size == record['bytes'], 'Checksum mismatch: ' + name
    return len(manifest['files'])


def verify(root, chess_path=None, no_manifest=False, manifest_only=False):
    checked_files = check_manifest(root) if not no_manifest else None
    if manifest_only:
        return {'manifest_files_checked': checked_files, 'status': 'passed'}
    if chess_path:
        sys.path.insert(0, str(chess_path))
    try:
        import chess
    except ImportError:
        sys.path.insert(0, str(root / 'harness'))
        from new_run import rules_library
        sys.path.insert(0, str(rules_library()))
        import chess
    import chess.pgn
    index = json.loads((root / 'data/index.json').read_text())
    games = {g['game_id']: g for g in rows(root / 'data/games.jsonl')}
    assert len(games) == index['totals']['game_session_starts']
    kinds = Counter((g['mode'], g['status']) for g in games.values())
    assert kinds['benchmark', 'scored'] == index['totals']['benchmark_scored']
    assert kinds['benchmark', 'active'] == index['totals']['benchmark_active']
    assert sum(g['mode'] == 'practice' for g in games.values()) == index['totals']['practice_sessions']
    assert kinds['match', 'scored'] == index['totals']['match_games']
    chains, ledger_events = 0, 0
    for run in index['runs']:
        for suffix in ('ledger.jsonl.gz', 'practice/ledger.jsonl.gz'):
            previous = '0' * 64
            for number, raw in enumerate(rows(root / 'data/runs' / run['run_id'] / suffix), 1):
                event = dict(raw)
                saved = event.pop('sha256')
                assert event['seq'] == number and event['previous'] == previous
                assert hashlib.sha256(canonical(event).encode()).hexdigest() == saved
                previous = saved
                ledger_events += 1
            chains += 1
    previous, match_events = '0' * 64, 0
    for number, event in enumerate(rows(root / 'data/match/events.jsonl.gz'), 1):
        body = {k: event[k] for k in ('at', 'kind', 'game', 'actor', 'payload', 'previous')}
        assert event['seq'] == number and event['previous'] == previous
        assert hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode()).hexdigest() == event['hash']
        previous = event['hash']
        match_events += 1
    snapshot_count = 0
    snapshot_refs = set()
    for entry in rows(root / 'data/snapshots.jsonl.gz'):
        path = root / 'data/runs' / entry['run_id'] / 'snapshots' / (entry['snapshot_id'] + '.tar.gz')
        listing = {}
        with tarfile.open(path, 'r|gz') as archive:
            for member in archive:
                assert member.isfile() and not member.name.startswith('/') and '..' not in Path(member.name).parts
                assert member.name not in listing
                with archive.extractfile(member) as stream:
                    listing[member.name] = hashlib.file_digest(stream, 'sha256').hexdigest()
        assert listing == entry['members']
        assert hashlib.sha256(canonical(listing).encode()).hexdigest() == entry['snapshot_id']
        snapshot_refs.add((entry['run_id'], entry['snapshot_id']))
        snapshot_count += 1
    assert snapshot_count == index['totals']['workspace_snapshots']
    for game in games.values():
        for key in ('start_snapshot', 'end_snapshot'):
            if game.get(key):
                assert (game['run_id'], game[key]) in snapshot_refs
    boards, plies, accepted_moves = {}, Counter(), 0
    for event in rows(root / 'data/moves.jsonl.gz'):
        identifier = event['game_id']
        game = games[identifier]
        board = boards.setdefault(identifier, chess.Board(game['initial_fen']))
        plies[identifier] += 1
        assert plies[identifier] == event['ply'], 'Ply gap: ' + identifier
        assert board.fen() == event['fen_before'], 'Before-FEN mismatch: ' + identifier
        move = chess.Move.from_uci(event['uci'])
        assert move in board.legal_moves and board.san(move) == event['san'], 'Illegal move/SAN: ' + identifier
        board.push(move)
        assert board.fen() == event['fen'], 'After-FEN mismatch: ' + identifier
        accepted_moves += 1
    assert accepted_moves == index['totals']['accepted_plies']
    for identifier, game in games.items():
        board = boards.get(identifier, chess.Board(game['initial_fen']))
        assert plies[identifier] == game['plies'] and board.fen() == game['final_fen']
    seen = set()
    with gzip.open(root / 'data/all-games.pgn.gz', 'rt', encoding='utf-8') as stream:
        while (record := chess.pgn.read_game(stream)) is not None:
            assert not record.errors
            identifier = record.headers['GameId']
            assert identifier not in seen and identifier in games
            seen.add(identifier)
            game = games[identifier]
            assert record.headers['Result'] == game['result']
            assert record.board().fen() == game['initial_fen']
            assert record.end().board().fen() == game['final_fen']
    assert len(seen) == len(games)
    trace_records, trace_count = 0, 0
    for trace in json.loads((root / 'data/traces/index.json').read_text()):
        count, record_types = 0, Counter()
        for number, entry in enumerate(rows(root / trace['path']), 1):
            assert entry['source_sequence'] == number and entry['run_id'] == trace['run_id']
            assert isinstance(entry['record'], dict)
            record_types[entry['kind']] += 1
            count += 1
        assert count == trace['records'] and dict(record_types) == trace['record_types']
        trace_records += count
        trace_count += 1
    assert trace_records == index['totals']['trace_records']
    return {'status': 'passed', 'manifest_files_checked': checked_files, 'game_sessions': len(games),
            'accepted_plies_replayed': accepted_moves, 'pgn_games_replayed': len(seen),
            'learning_ledger_chains': chains, 'learning_ledger_events': ledger_events,
            'match_ledger_events': match_events, 'workspace_snapshots_verified': snapshot_count,
            'trace_files': trace_count, 'trace_records_parsed': trace_records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--chess-path', type=Path, help='Optional path containing an existing chess package')
    parser.add_argument('--no-manifest', action='store_true', help='Check data before creating a release manifest')
    parser.add_argument('--manifest-only', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    report = verify(args.root.resolve(), args.chess_path, args.no_manifest, args.manifest_only)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
