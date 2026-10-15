#!/usr/bin/env python3
"""Verify frozen audit sources and fixed measurement controls; no engine calls."""
from pathlib import Path
import collections
import datetime as dt
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SNAP = HERE / 'measurement/snapshots'


def digest(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def read_chain(path):
    events, previous = [], '0' * 64
    for number, line in enumerate(path.open(), 1):
        event = json.loads(line)
        body = {k: v for k, v in event.items() if k != 'sha256'}
        encoded = json.dumps(body, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
        assert event['seq'] == number, (path, number, 'sequence')
        assert event['previous'] == previous, (path, number, 'previous')
        assert hashlib.sha256(encoded).hexdigest() == event['sha256'], (path, number, 'hash')
        previous = event['sha256']
        events.append(event)
    return events, previous


def main():
    manifest = json.loads((SNAP / 'manifest.json').read_text())
    result = {'verified_at': dt.datetime.now(dt.timezone.utc).isoformat(),
              'snapshot_at': manifest['capturedAt'], 'runs': {},
              'scope': 'Frozen-file SHA256, append-only hash chains, all benchmark start settings, current pinned-file hashes. Does not inspect hidden reasoning, invoke engines or modify experiment files.',
              'limits': 'Hash chains and pinned files detect ordinary changes. Shared-account logs are not an adversarial guarantee and do not prove absence of unrecorded activity.'}
    for slug, item in manifest['runs'].items():
        folder = ROOT / item['name']
        for rel, meta in item['files'].items():
            assert digest(SNAP / slug / rel) == meta['sha256'], (slug, rel, 'frozen mismatch')
        cfg = json.loads((SNAP / slug / '.arena/config.json').read_text())
        events, head = read_chain(SNAP / slug / 'data/ledger.jsonl')
        practice, practice_head = read_chain(SNAP / slug / 'data/practice/ledger.jsonl')
        starts = [e for e in events if e['kind'] == 'start']
        results = [e for e in events if e['kind'] == 'result']
        for n, event in enumerate(starts):
            assert event['game'] == n + 1, (slug, n, 'game numbering')
            assert event['opponent'] == cfg['opponents'][(n // 2) % 3], (slug, n, 'opponent')
            assert event['color'] == ('white' if n % 2 == 0 else 'black'), (slug, n, 'color')
            assert event['nodes_per_move'] == cfg['nodes_per_move'] == 1000000, (slug, n, 'nodes')
        assert len({e['game'] for e in results}) == len(results), (slug, 'duplicate result')
        original_manifest = json.loads((folder / '.arena/manifest.json').read_text())
        pinned_mismatches = [p for p, expected in original_manifest.items()
                             if not (folder / p).is_file() or digest(folder / p) != expected]
        assert not pinned_mismatches, (slug, pinned_mismatches)
        updates = [{k: e[k] for k in ('kind', 'game', 'timestamp', 'description', 'reason', 'change') if k in e}
                   for e in events if e['kind'] not in ('start', 'move', 'illegal', 'result', 'note', 'usage', 'engine_error')]
        result['runs'][slug] = {
            'starts': len(starts), 'scored': sum(e['score'] is not None for e in results),
            'unscored_results': sum(e['score'] is None for e in results),
            'active': len(starts) - len(results), 'benchmark_events': len(events),
            'benchmark_head': head, 'practice_head': practice_head,
            'practice_events': len(practice),
            'illegal_submissions': sum(e['kind'] == 'illegal' for e in events),
            'illegal_forfeits': sum(e.get('reason') == 'illegal_move_forfeit' for e in results),
            'engine_errors': sum(e['kind'] == 'engine_error' for e in events),
            'terminal_reasons': dict(collections.Counter(e['reason'] for e in results)),
            'pinned_files_verified': len(original_manifest), 'pinned_mismatches': pinned_mismatches,
            'benchmark_schedule_nodes_options_colors_verified': True,
            'source_ledger_unchanged_since_freeze': digest(folder / 'data/ledger.jsonl') == item['files']['data/ledger.jsonl']['sha256'],
            'operator_events': updates,
            'first_timestamp': events[0]['timestamp'], 'last_timestamp': events[-1]['timestamp']}
    (HERE / 'source-verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: {a: v[a] for a in ('starts', 'scored', 'active', 'illegal_submissions', 'illegal_forfeits', 'engine_errors', 'pinned_files_verified')} for k, v in result['runs'].items()}, indent=2))


if __name__ == '__main__':
    main()
