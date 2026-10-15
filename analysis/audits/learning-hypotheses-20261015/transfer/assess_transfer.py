#!/usr/bin/env python3
"""Retrospective mechanical replay and authored-note chronology; never runs engines.

Reads the common frozen measurement manifest and immutable workspace archives.
Only named public authored notes are decoded. No private reasoning is read.
"""
from __future__ import annotations

import collections
import datetime as dt
import hashlib
import importlib.util
import json
import re
import statistics
import sys
import tarfile
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/home/peter/Chess Learning')
OUT = ROOT / '.operator/audits/learning-hypotheses-20261015/transfer'
SNAPS = OUT.parent / 'measurement/snapshots'
CONFIG = {
    'astra': ('Chess - GPT-6-Astra', ['learning-journal.md', 'move-check.md', 'geometry-cards.md']),
    'sol': ('Chess - GPT-6.1-Sol', ['journal.md']),
    'sol-long': ('Chess - GPT-6.1-Sol - Long Context', ['learning.md']),
    'sol-long-max': ('Chess - GPT-6.1-Sol - Long Context - Max', ['learning.md']),
    'opus': ('Chess - Opus-5.5', []),
    'fable': ('Chess - Fable-5.1', []),
}


def digest_bytes(value):
    return hashlib.sha256(value).hexdigest()


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


spec = importlib.util.spec_from_file_location('mechanical_assessment', ROOT / '.operator/learning-assessment/assess.py')
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)


def selected_run(manifest, slug):
    # A later resumed freeze may label endpoints in the slug. Never use live ledgers.
    candidates = [slug, {'astra': 'astra200', 'sol': 'sol200', 'sol-long': 'sol-long99',
                        'sol-long-max': 'sol-long-max63', 'fable': 'fable45', 'opus': 'opus200'}[slug]]
    return next(k for k in reversed(candidates) if k in manifest['runs'])


def read_games(manifest, slug, path):
    info = manifest['runs'][selected_run(manifest, slug)]['files'][path]
    p = Path(info['snapshot'])
    assert digest_bytes(p.read_bytes()) == info['sha256'], (slug, path, 'manifest file digest')
    events, chain = a.read_ledger(p)
    assert chain['head'] == info['head']
    games = a.group_games(events)
    for g in games:
        g['features'] = a.replay(g)
    return games, {'file': str(p), 'sha256': info['sha256'], **chain}


def fraction(n, total):
    return n / total if total else None


def distribution(values):
    return {'n': len(values), 'sum': sum(values), 'median': statistics.median(values) if values else None,
            'min': min(values) if values else None, 'max': max(values) if values else None,
            'counts': dict(sorted(collections.Counter(values).items()))}


def game_summary(gs):
    answer = {'gameNumbers': [g['start']['game'] for g in gs], 'score': a.tally(gs),
              'behavior': a.behavior(gs), 'byOpponent': {}}
    answer['firstMoves'] = dict(collections.Counter(f"{g['start']['color']}:{g['features']['firstMove']}" for g in gs))
    answer['queenMovesFirst10Mean'] = statistics.mean(g['features']['queenMovesFirst10'] for g in gs) if gs else None
    for opponent in a.OPPONENTS:
        group = [g for g in gs if g['start']['opponent']['id'] == opponent]
        answer['byOpponent'][opponent] = {'score': a.tally(group), 'behavior': a.behavior(group)}
    # Exposures are accepted own moves in each horizon; proxy events are assigned
    # to the own move immediately preceding the opponent's capture.
    phases = {'ownMoves1to15': {'ownMoves': 0, 'shortLossCount': 0},
              'ownMoves16plus': {'ownMoves': 0, 'shortLossCount': 0}}
    for g in gs:
        own = g['features']['ownMoves']
        phases['ownMoves1to15']['ownMoves'] += min(own, 15)
        phases['ownMoves16plus']['ownMoves'] += max(own - 15, 0)
        for loss in g['features']['shortLosses']:
            previous_index = loss['ply'] - 2
            n = sum(e['actor'] == 'model' for e in g['moves'][:previous_index + 1])
            phases['ownMoves1to15' if n <= 15 else 'ownMoves16plus']['shortLossCount'] += 1
    for phase in phases.values():
        phase['shortLossPer100'] = 100 * fraction(phase['shortLossCount'], phase['ownMoves']) if phase['ownMoves'] else None
    answer['materialLossPhases'] = phases
    return answer


def practice_summary(practices, benchmarks):
    last_end = max(g['end']['timestamp'] for g in benchmarks if g['end'])
    # The common endpoint freeze includes practices up to the paused next game;
    # report all retained sessions, plus chronology relative to benchmark result.
    scored = [p for p in practices if p['end'] and p['end']['score'] is not None]
    stopped = [p for p in practices if p['end'] and p['end']['score'] is None]
    half = len(practices) // 2
    records = []
    originals = {g['start']['game']: g for g in benchmarks}
    for p in practices:
        initial = a.chess.Board(p['start'].get('initial_fen', a.chess.STARTING_FEN))
        own_color = p['start']['color'] == 'white'
        source = p['start'].get('source', {})
        original = originals.get(source.get('game')) if source.get('kind') == 'benchmark' else None
        suffix = original['moves'][source['ply']:] if original else None
        played = [e['uci'] for e in p['moves']]
        original_prefix = [e['uci'] for e in suffix[:len(played)]] if suffix is not None else None
        records.append({'practice': p['start']['game'], 'timestamp': p['start']['timestamp'],
                        'origin': p['start'].get('source'), 'initialMaterial': a.material(initial, own_color),
                        'opponent': p['start']['opponent']['id'], 'note': p['start'].get('note'),
                        'ownMoves': p['features']['ownMoves'], 'plies': len(p['moves']),
                        'illegal': len(p['illegal']), 'score': p['end']['score'] if p['end'] else None,
                        'reason': p['end']['reason'] if p['end'] else None,
                        'shortLosses': p['features']['shortLosses'],
                        'sourceBenchmarkScore': original['end']['score'] if original and original['end'] else None,
                        'sameCompleteMovePrefixAsSource': played == original_prefix if played and original_prefix is not None else None,
                        'afterLastBenchmarkResult': p['start']['timestamp'] > last_end})
    return {'started': len(practices), 'scored': a.tally(scored), 'stopped': len(stopped),
            'active': sum(p['end'] is None for p in practices),
            'origins': dict(collections.Counter(p['start'].get('source', {}).get('kind', 'unknown') for p in practices)),
            'opponents': dict(collections.Counter(p['start']['opponent']['id'] for p in practices)),
            'ownMoveLengths': distribution([p['features']['ownMoves'] for p in practices]),
            'scoredOwnMoveLengths': distribution([p['features']['ownMoves'] for p in scored]),
            'stoppedOwnMoveLengths': distribution([p['features']['ownMoves'] for p in stopped]),
            'firstHalfOwnMoveLengths': distribution([p['features']['ownMoves'] for p in practices[:half]]),
            'lastHalfOwnMoveLengths': distribution([p['features']['ownMoves'] for p in practices[-half:]]) if half else None,
            'atMost2OwnMoves': sum(p['features']['ownMoves'] <= 2 for p in practices),
            'atMost4OwnMoves': sum(p['features']['ownMoves'] <= 4 for p in practices),
            'atMost8OwnMoves': sum(p['features']['ownMoves'] <= 8 for p in practices),
            'initialMaterial': distribution([r['initialMaterial'] for r in records]),
            'scoredWins': [r for r in records if r['score'] == 1],
            'sameCompleteMovePrefixAsSource': sum(r['sameCompleteMovePrefixAsSource'] is True for r in records),
            'practiceBehavior': a.behavior(practices), 'records': records}


def archive_notes(folder, snapshot, names):
    path = folder / 'data/snapshots' / f'{snapshot}.tar.gz'
    listing, notes = {}, {}
    with tarfile.open(path, 'r:gz') as archive:
        for entry in archive:
            assert entry.isfile() and not entry.issym() and entry.size <= 32 * 1024 ** 2
            value = archive.extractfile(entry).read()
            listing[entry.name] = digest_bytes(value)
            if entry.name in names:
                notes[entry.name] = value.decode()
    assert digest_bytes(a.canonical(listing).encode()) == snapshot, ('workspace archive digest', str(path))
    return notes, listing


def note_chronology(slug, benchmark_games, profiles):
    folder_name, filenames = CONFIG[slug]
    if not filenames:
        return {}
    folder = ROOT / folder_name
    history, latest, versions, archive_cache, review_files = {}, {}, [], {}, {}
    for g in benchmark_games:
        start = g['start']; snapshot = start['snapshot']
        if snapshot not in archive_cache:
            archive_cache[snapshot] = archive_notes(folder, snapshot, filenames)
        texts, listing = archive_cache[snapshot]
        history[start['game']] = texts
        sizes = {name: {'bytes': len(text.encode()), 'words': len(text.split()), 'sha256': digest_bytes(text.encode())}
                 for name, text in texts.items()}
        versions.append({'game': start['game'], 'timestamp': start['timestamp'], 'snapshot': snapshot, 'files': sizes})
        latest = texts
        if slug == 'sol':
            # Track later authored per-game reviews by snapshot membership only.
            for name in listing:
                if re.fullmatch(r'review\d+\.md', name) and name not in review_files:
                    review_files[name] = {'firstBeforeGame': start['game'], 'snapshot': snapshot,
                                          'sha256': listing[name]}
    output_notes = OUT / 'notes' / slug
    for name, text in latest.items():
        p = output_notes / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    profile_key = 'sol-long-context' if slug == 'sol-long' else slug
    changes = []
    blocks = a.complete_rotations([g for g in benchmark_games if g['end'] and g['end']['score'] is not None])
    candidates = profiles.get(profile_key, {}).get('changes', [])
    if slug == 'sol-long-max':
        candidates = [
            {'title': 'Shorten speculative branches and verify destination', 'file': 'learning.md',
             'marker': '### Trial 5: Shorten speculative branches and verify the actual destination'},
            {'title': 'Immediate checks on resulting board', 'file': 'learning.md',
             'marker': "### Trial 6: Verify the opponent's immediate checks on the resulting board"},
            {'title': 'Retain a blocker while changing king shelter', 'file': 'learning.md',
             'marker': '### Trial 44: retain a blocker while changing king shelter'}]
    for change in candidates:
        match = next(((n, texts[change['file']]) for n, texts in sorted(history.items())
                      if change['file'] in texts and change['marker'] in texts[change['file']]), None)
        item = dict(change)
        item['firstVerifiedBeforeGame'] = match[0] if match else None
        if match:
            number, text = match
            item['source'] = versions[next(i for i, v in enumerate(versions) if v['game'] == number)]
            marker_pos = text.index(change['marker'])
            item['excerpt'] = text[marker_pos:marker_pos + 1800]
            before = [b for b in blocks if b[-1]['start']['game'] < number][-2:]
            after_blocks = [b for b in blocks if b[0]['start']['game'] >= number]
            after = after_blocks[:2]
            common = min(len(before), len(after))
            item['localTransfer'] = {'before': game_summary([g for b in before[-common:] for g in b]) if common else None,
                                     'after': game_summary([g for b in after[:common] for g in b]) if common else None,
                                     'retentionNext2Rotations': game_summary([g for b in after_blocks[2:4] for g in b])}
        changes.append(item)
    return {'source': 'Hash-verified authored files within recorded benchmark-start workspace snapshots',
            'history': versions, 'strategyChanges': changes, 'latestNoteCopies': {n: str(output_notes / n) for n in latest},
            'laterReviewFirstAppearance': review_files,
            'limitations': ['The final completed game may have notes written afterward, absent from its start snapshot.',
                            'Declarations and short local event studies do not identify causal effects.',
                            'Two-rotation local windows overlap between nearby interventions and are exploratory.']}


def main():
    manifest_path = SNAPS / 'manifest.json'
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    profiles = json.loads((ROOT / '.operator/learning-assessment/strategy-register.json').read_text())
    report = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'manifestSha256': digest_bytes(manifest_bytes),
              'manifestCapturedAt': manifest.get('capturedAt'), 'method': __doc__, 'runs': {},
              'limitations': ['No model weights or training gradients were measured; adaptation means changed decisions or external memory.',
                              'Short-horizon material loss is mechanical: a nonpawn piece is captured and at least 2 net points remain lost after the next own reply. Sacrifices and compensation can qualify.',
                              'Terminal opponent captures lacking a following own reply are excluded from that proxy.',
                              'Practice sessions are selected, heterogeneous and often stopped; they are not independent held-out tests.',
                              'A rate per own move can differ from a rate per game; both denominators are retained.',
                              'No chess engine, learner, hidden reasoning transcript, or external source was invoked.']}
    for slug in CONFIG:
        games, chain = read_games(manifest, slug, 'data/ledger.jsonl')
        practice, practice_chain = read_games(manifest, slug, 'data/practice/ledger.jsonl')
        completed = [g for g in games if g['end'] and g['end']['score'] is not None]
        blocks = a.complete_rotations(completed)
        size = len(blocks) // 2
        early = [g for b in blocks[:size] for g in b]
        late = [g for b in blocks[-size:] for g in b] if size else []
        result = {'ledger': chain, 'practiceLedger': practice_chain,
                  'overall': game_summary(completed),
                  'matchedHalves': {'rotationsPerWindow': size, 'early': game_summary(early), 'late': game_summary(late)},
                  'practice': practice_summary(practice, completed),
                  'notes': note_chronology(slug, games, profiles),
                  'shortLossExamples': [{'game': g['start']['game'], 'opponent': g['start']['opponent']['id'], **loss}
                                        for g in completed for loss in g['features']['shortLosses']],
                  'illegalExamples': [{k: e[k] for k in ('game', 'ply', 'submitted', 'timestamp')} for g in completed for e in g['illegal']]}
        report['runs'][slug] = result
        dump(OUT / f'{slug}.json', result)
        p = result['practice']; e = result['matchedHalves']['early']['behavior']; l = result['matchedHalves']['late']['behavior']
        print(f"{slug}: {len(completed)} benchmark; practice {p['started']} scored {p['scored']['games']} stopped {p['stopped']} median-own {p['ownMoveLengths']['median']}; matched illegal/100 {e['illegalPer100']:.3f}->{l['illegalPer100']:.3f}, short-loss/100 {e['shortLossPer100']:.3f}->{l['shortLossPer100']:.3f}")
    # Existing structured context assessment is copied with its own provenance;
    # this is secondary evidence, not a re-read of private transcripts.
    context_paths = [ROOT / '.operator/audits/astra-context-20261008/context-assessment.json',
                     ROOT / '.operator/audits/astra-context-20261008/run-summary.json',
                     ROOT / '.operator/audits/sol-828k-20261006-1646/audit.json']
    context = {}
    for p in context_paths:
        value = p.read_bytes(); content = json.loads(value)
        context[p.name] = {'source': str(p), 'sha256': digest_bytes(value)}
        if p.name == 'context-assessment.json':
            context[p.name]['data'] = {k: content[k] for k in ['method', 'comparisons', 'compactions', 'gameContextBins',
                                                              'postCompactionMaterialProxy', 'selectedErrorContextExamples',
                                                              'historicalNoteSizes', 'limitations']}
        elif p.name == 'run-summary.json':
            context[p.name]['data'] = {k: content[k] for k in content if k != 'byGame'}
        else:
            context[p.name]['data'] = {'at': content['at'], 'method': content['method'],
                                      'runs': {k: {f: v[f] for f in ['folder', 'completed', 'actualEfforts', 'appliedSettings',
                                                                    'compactions', 'latestOccupancy', 'firstGameInputTokenRange']}
                                               | {'matchedMoveUsage': {f: x for f, x in v['matchedMoveUsage'].items() if f != 'matches'}}
                                               for k, v in content['runs'].items()}}
    dump(OUT / 'context-secondary.json', context)
    report['secondaryContextSources'] = {k: {f: v[f] for f in ('source', 'sha256')} for k, v in context.items()}
    dump(OUT / 'results.json', report)


if __name__ == '__main__':
    main()
