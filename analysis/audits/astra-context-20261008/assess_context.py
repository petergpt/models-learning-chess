#!/usr/bin/env python3
"""Audit observable context/notes use in the frozen original Astra run.

Only usage/configuration metadata, compaction timestamps and observable tool
commands/results are inspected. Reasoning items and compacted text are skipped.
No engine, player session or measurement file is changed.
"""
from __future__ import annotations

import ast
import bisect
import collections
import datetime as dt
import hashlib
import importlib.util
import json
import math
import re
import statistics
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/home/peter/Chess Learning')
HERE = Path(__file__).resolve().parent
FOLDER = ROOT / 'Chess - GPT-6-Astra'
spec = importlib.util.spec_from_file_location('learning_assessment', ROOT / '.operator/learning-assessment/assess.py')
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
events, integrity = a.read_ledger(FOLDER / 'data/ledger.jsonl')
games = a.group_games(events)
assert len(games) == 200 and all(g['end'] for g in games)
source = json.loads((ROOT / 'Matches/Astra vs Opus - 30 games/.operator/setup.json').read_text())['players']['astra']
native = Path(source['nativePath'])

def ts(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00')).timestamp()

def sha(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()

start_times = [ts(g['start']['timestamp']) for g in games]
end_times = [ts(g['end']['timestamp']) for g in games]

def during_game(t):
    i = bisect.bisect_right(start_times, t) - 1
    return games[i]['start']['game'] if i >= 0 and t <= end_times[i] else None

def next_game(t):
    i = bisect.bisect_right(start_times, t) - 1
    if i >= 0 and t <= end_times[i]:
        return games[i]['start']['game']
    i += 1
    return games[i]['start']['game'] if i < len(games) else None

NAMES = ('learning-journal.md', 'geometry-cards.md', 'move-check.md')
CMD = re.compile(r'\bcmd\s*:\s*("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`[^`]*`)')

def commands(text):
    found = []
    for match in CMD.finditer(text):
        raw = match.group(1)
        try:
            found.append(ast.literal_eval(raw) if not raw.startswith('`') else raw[1:-1])
        except (ValueError, SyntaxError):
            pass
    return found

def read_candidate(cmd):
    """Conservative detector; never executes historical commands."""
    if not any(name in cmd for name in NAMES):
        return False
    # Restrict Python reads to printed content, excluding updates and bookkeeping.
    if re.match(r'\s*python3?\b', cmd):
        return (bool(re.search(r'\bprint\s*\(', cmd))
                and any(s in cmd for s in ('read_text(', '.read(', 'open('))
                and not any(s in cmd for s in ('write_text(', 'write_bytes(', '.write(')))
    # Ignore the heredoc body: a journal write is not a journal read.
    shell = cmd.split('<<', 1)[0]
    for part in re.split(r'\s*(?:&&|;|\|\|)\s*', shell):
        if not any(name in part for name in NAMES):
            continue
        if re.match(r'\s*cat\b', part) and '>' not in part:
            return True
        if re.match(r'\s*(?:tail|head)\b', part) and '>' not in part:
            return True
        if re.match(r'\s*sed\b', part) and not re.search(r'\s-i\b', part) and '>' not in part:
            return True
        if re.match(r'\s*rg\b', part) and '--files' not in part and '>' not in part:
            return True
    return False

def mode(cmd, name):
    if name not in cmd:
        return None
    if re.match(r'\s*python3?\b', cmd):
        return 'bounded-python-excerpt' if re.search(r'\[\s*-|splitlines\(', cmd) else 'python-inspection'
    for part in re.split(r'\s*(?:&&|;|\|\|)\s*', cmd.split('<<', 1)[0]):
        if name not in part:
            continue
        if re.match(r'\s*cat\b', part) and '>' not in part:
            return 'whole-file'
        if re.match(r'\s*(tail|head|sed)\b', part) and '>' not in part:
            return 'bounded-excerpt'
        if re.match(r'\s*rg\b', part) and '--files' not in part:
            return 'search'
    return None

def output_strings(value):
    """Unwrap only observable tool output, not passthrough metadata."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for block in value:
            if isinstance(block, dict) and block.get('type') in ('input_text', 'text'):
                yield block.get('text', '')

def shell_results(value):
    """Find structured exec_command result objects, without retaining text."""
    if isinstance(value, dict):
        if isinstance(value.get('output'), str) and any(k in value for k in ('exit_code', 'session_id', 'original_token_count')):
            output = value['output']
            yield {'words': len(output.split()), 'characters': len(output),
                   'originalTokenCount': value.get('original_token_count'),
                   'exitCode': value.get('exit_code'), 'running': value.get('session_id') is not None,
                   'truncated': bool(re.search(r'(?:truncated|omitted)\s+(?:output|lines)|output\s+(?:is\s+)?truncated|tokens\s+truncated', output, re.I))}
        else:
            for child in value.values():
                yield from shell_results(child)
    elif isinstance(value, list):
        for child in value:
            yield from shell_results(child)

usage, compactions, reads, context_counters = [], [], [], []
usage_ids, windows = set(), set()
pending, all_calls = {}, {}
cumulative = None
for line in native.open():
    event = json.loads(line)
    kind = event['type']
    t = ts(event['timestamp'])
    if kind == 'compacted':
        # Do not access the compacted payload or summary text.
        compactions.append(t)
        continue
    if kind not in ('token_usage_record', 'event_msg', 'response_item'):
        continue
    payload = event.get('payload', {})
    if kind == 'token_usage_record':
        rid = payload['response_id']
        assert rid not in usage_ids
        usage_ids.add(rid)
        u = payload['usage']
        usage.append({'t': t, 'timestamp': event['timestamp'], 'game': during_game(t),
                      'input': u['input_tokens'], 'cached': u.get('cached_input_tokens', 0),
                      'output': u['output_tokens'], 'reasoning': u.get('reasoning_output_tokens', 0)})
        cumulative = payload.get('thread_token_usage')
    elif kind == 'event_msg' and payload.get('type') == 'token_count':
        window = (payload.get('info') or {}).get('model_context_window')
        if window:
            windows.add(window)
    elif kind == 'response_item':
        tp = payload.get('type')
        # Skip all reasoning and assistant message content.
        if tp in ('custom_tool_call', 'function_call'):
            inp = payload.get('input', payload.get('arguments', ''))
            if not isinstance(inp, str):
                continue
            read_cmds = [cmd for cmd in commands(inp) if read_candidate(cmd)]
            counter = 'get_context_remaining' in inp
            if not read_cmds and not counter:
                continue
            call_id = payload.get('call_id')
            record = {'timestamp': event['timestamp'], 'game': during_game(t), 'nextBenchmark': next_game(t),
                      'commands': read_cmds, 'hasContextCounter': counter, 'outputResults': []}
            pending[call_id] = record
            all_calls[call_id] = record
            if read_cmds:
                reads.append(record)
        elif tp in ('custom_tool_call_output', 'function_call_output') and payload.get('call_id') in pending:
            call = pending.pop(payload['call_id'])
            for text in output_strings(payload.get('output')):
                try:
                    obj = json.loads(text)
                except (ValueError, TypeError):
                    continue
                call['outputResults'].extend(shell_results(obj))
                if call['hasContextCounter']:
                    # Read only the numeric token counter from nested output.
                    def counters(o):
                        if isinstance(o, dict):
                            if isinstance(o.get('tokens_left'), (int, float)):
                                yield o['tokens_left']
                            for v in o.values():
                                yield from counters(v)
                        elif isinstance(o, list):
                            for v in o:
                                yield from counters(v)
                    context_counters.extend({'timestamp': event['timestamp'], 'tokensLeft': n,
                                             'game': during_game(t), 'nextBenchmark': next_game(t)} for n in counters(obj))

assert len(windows) == 1
WINDOW = next(iter(windows))
assert all(0 <= u['cached'] <= u['input'] for u in usage)
assert sum(u['input'] for u in usage) == cumulative['input_tokens']
assert sum(u['reasoning'] for u in usage) == cumulative['reasoning_output_tokens']
assert all(usage[i]['t'] <= usage[i+1]['t'] for i in range(len(usage)-1))
usage_times = [u['t'] for u in usage]
compactions.sort()

def stats(values):
    if not values:
        return None
    v = sorted(values)
    return {'count': len(v), 'mean': statistics.mean(v), 'median': statistics.median(v),
            'p10': a.quantile(v, .1), 'p90': a.quantile(v, .9), 'min': v[0], 'max': v[-1]}

game_rows = []
own_move_records = sorted((ts(m['timestamp']), g['start']['game'], m['ply'])
                          for g in games for m in g['moves'] if m['actor']=='model')
own_move_times = [x[0] for x in own_move_records]
def latest_input(t):
    i = bisect.bisect_right(usage_times, t)-1
    return usage[i]['input'] if i >= 0 else None

for g in games:
    n = g['start']['game']
    own_moves = [m for m in g['moves'] if m['actor'] == 'model']
    us = [u for u in usage if u['game'] == n]
    g['features'] = a.replay(g)
    game_rows.append({'game': n, 'opponent': g['start']['opponent']['id'], 'color': g['start']['color'],
                      'score': g['end']['score'], 'ownMoves': len(own_moves),
                      'prompt': stats([u['input'] for u in us]),
                      'firstAcceptedMovePrecedingInputTokens': latest_input(ts(own_moves[0]['timestamp'])),
                      'reasoningTokensPerMove': sum(u['reasoning'] for u in us)/len(own_moves),
                      'compactionsDuringGame': sum(start_times[n-1] <= c <= end_times[n-1] for c in compactions),
                      'shortLossCount': len(g['features']['shortLosses']),
                      'illegal': len(g['illegal'])})

comparisons = []
for lo, hi in [(1,96), (103,198), (1,50), (51,100), (101,150), (151,200)]:
    gs = [g for g in game_rows if lo <= g['game'] <= hi and g['opponent'] in a.RATED]
    nums = {g['game'] for g in gs}
    us = [u for u in usage if u['game'] in nums]
    rs = [r for r in reads if r['nextBenchmark'] and lo <= r['nextBenchmark'] <= hi]
    read_modes = collections.defaultdict(collections.Counter)
    for r in rs:
        for cmd in r['commands']:
            for name in NAMES:
                m = mode(cmd, name)
                if m:
                    read_modes[name][m] += 1
    outputs = [o for r in rs for o in r['outputResults'] if o['exitCode'] == 0 and not o['running']]
    comparisons.append({'games': [lo,hi], 'ratedGames': len(gs), 'modelResponsesDuringRatedGames': len(us),
                        'pointScore': statistics.mean(g['score'] for g in gs),
                        'inputTokensPerResponse': stats([u['input'] for u in us]),
                        'fractionOfResponsesOver180k': sum(u['input'] >= 180000 for u in us)/len(us),
                        'fractionOfResponsesOver200k': sum(u['input'] >= 200000 for u in us)/len(us),
                        'fractionOfResponsesOver90pctOfWindow': sum(u['input'] >= .9*WINDOW for u in us)/len(us),
                        'reasoningTokensPerAcceptedMove': sum(u['reasoning'] for u in us)/sum(g['ownMoves'] for g in gs),
                        'compactionsInWholeBenchmarkPeriod': sum(start_times[lo-1] <= c <= end_times[hi-1] for c in compactions),
                        'noteReadToolCallsIncludingBetweenGameStudy': len(rs),
                        'noteReadModes': {k:dict(v) for k,v in read_modes.items()},
                        'readCallOutputWordsIncludingOtherBatchedCommands': stats([o['words'] for o in outputs]),
                        'readCallReportedOutputTokensIncludingOtherBatchedCommands': stats([o['originalTokenCount'] for o in outputs if o['originalTokenCount'] is not None]),
                        'readCallOutputTruncations': sum(o['truncated'] for o in outputs)})

# First observed response after each compaction; do not inspect summary quality.
after_compact = []
for c in compactions:
    j = bisect.bisect_right(usage_times, c)
    if j < len(usage):
        u = usage[j]
        after_compact.append({'timestamp': dt.datetime.fromtimestamp(c, dt.timezone.utc).isoformat(),
                              'nextBenchmark': next_game(c), 'nextInputTokens': u['input'],
                              'previousInputTokens': usage[j-1]['input'] if j else None})

# Game-level context comparison within opponent and broad early/late periods.
# These are observational bins, not causal effects or move-quality measurements.
context_bins = []
for lo,hi in [(1,96),(103,198)]:
    for op in a.RATED:
        for measure in ['average-game-input','first-accepted-move-input']:
            # Split separately in each colour so both halves remain balanced.
            groups = collections.defaultdict(list)
            for color in ('white','black'):
                ordered = sorted([g for g in game_rows if lo <= g['game'] <= hi and g['opponent'] == op and g['color']==color],
                                 key=lambda g:g['prompt']['mean'] if measure=='average-game-input' else g['firstAcceptedMovePrecedingInputTokens'])
                cut = len(ordered)//2
                groups['lower-half'].extend(ordered[:cut])
                groups['upper-half'].extend(ordered[cut:])
            context_bins.append({'games':[lo,hi], 'opponent':op, 'measure':measure,
                                 'groups':[{'label':label,'games':sorted(g['game'] for g in selected),
                                            'meanPrompt':statistics.mean(g['prompt']['mean'] if measure=='average-game-input' else g['firstAcceptedMovePrecedingInputTokens'] for g in selected),
                                            'pointScore':statistics.mean(g['score'] for g in selected)}
                                           for label,selected in groups.items()]})

# Accepted own moves before/after any logged compaction. A short material loss is
# merely a mechanical proxy and may include deliberate sacrifices.
post_compaction_counts = collections.defaultdict(lambda: {'ownMoves':0,'shortLossCount':0})
for g in games:
    n = g['start']['game']
    if g['start']['opponent']['id'] not in a.RATED or not (n<=96 or 103<=n<=198):
        continue
    period = 'early' if n <= 96 else 'late'
    short_loss_preceding_own_plies = {x['ply']-1 for x in g['features']['shortLosses']}
    for m in (m for m in g['moves'] if m['actor']=='model'):
        t = ts(m['timestamp'])
        j = bisect.bisect_right(compactions, t)-1
        # Count globally across benchmark games, so an old compaction is not
        # repeatedly treated as fresh at the start of each subsequent game.
        if j >= 0:
            since = bisect.bisect_right(own_move_times,t)-bisect.bisect_right(own_move_times,compactions[j])
            near = since <= 5
        else:
            near = False
        key = f'{period}:{"first-five-after-compaction" if near else "other-moves"}'
        post_compaction_counts[key]['ownMoves'] += 1
        post_compaction_counts[key]['shortLossCount'] += m['ply'] in short_loss_preceding_own_plies
for v in post_compaction_counts.values():
    v['shortLossPer100OwnMoves'] = 100*v['shortLossCount']/v['ownMoves']
assert sum(v['ownMoves'] for k,v in post_compaction_counts.items() if k.endswith('first-five-after-compaction')) <= 5*len(compactions)

error_context_examples=[]
for number,kind,needle,description in [
    (4,'illegal','d4c5','Backward Black-pawn recapture'),
    (173,'illegal','h4g3','Backward White-pawn recapture'),
    (173,'illegal','h2h7','Rook path blocked by its own king'),
    (197,'move','c7c8q','Queen promotion resulted in stalemate'),
    (198,'move','e6f5','Bishop moved to capturable f5 with blocked imagined rook recapture')]:
    g=games[number-1]
    candidates=[e for e in events if e.get('game')==number and e['kind']==kind and (e.get('uci')==needle or e.get('submitted')==needle)]
    # Keep missing candidates visible rather than invent matching positions.
    if not candidates:
        error_context_examples.append({'game':number,'description':description,'notLocatedByUci':needle})
        continue
    for e in candidates:
        t=ts(e['timestamp']); j=bisect.bisect_right(compactions,t)-1
        error_context_examples.append({'game':number,'description':description,'kind':kind,'uci':needle,'ply':e.get('ply'),
                                       'precedingResponseInputTokens':latest_input(t),
                                       'acceptedBenchmarkOwnMovesSinceLastCompaction':bisect.bisect_right(own_move_times,t)-bisect.bisect_right(own_move_times,compactions[j]) if j>=0 else None,
                                       'minutesSinceLastCompaction':(t-compactions[j])/60 if j>=0 else None})

assert sha(native) == source['sourceNativeSha256']
assert sha(FOLDER/'data/ledger.jsonl') == source['sourceLedgerSha256']
old = json.loads((ROOT/'.operator/audits/astra-learning-20261008/reasoning-usage.json').read_text())
for existing in old['windows']:
    if existing['opponent']=='all-rated':
        got=next(x for x in comparisons if x['games']==existing['games'])
        assert abs(got['reasoningTokensPerAcceptedMove']-existing['reasoningTokensPerAcceptedMove']) < 1e-9

report = {'subject':'Original GPT-6 Astra 200-game run, context hypothesis',
          'method':{'readOnly':True, 'hiddenReasoningOrCompactionTextInspected':False,
                    'usageRecords':len(usage),'usageUniqueIds':len(usage_ids),
                    'usageSumsMatchFinalThreadCumulative':True,'sourceHashesUnchanged':True,
                    'recordedContextWindow':WINDOW,
                    'promptMeasure':'Input tokens per native model-response usage record, including cached input. This measures input length, not how much was attended to or retained correctly.',
                    'noteReadDetector':'Statically extract literal cmd arguments and classify nonmutating cat/tail/head/sed/rg or Python printed file reads. No historical commands executed. Dynamic and indirect reads may not be captured.',
                    'noteOutputScope':'Whole observable exec results in note-reading batches; includes accompanying rules/goal/trial/PGN output. Not an exact count of journal tokens.',
                    'postCompactionScope':'Next five accepted own benchmark moves after a compaction, counted globally across benchmark games; practice moves are excluded. Material-loss proxy is not an engine judgment; observations are clustered and exploratory.'},
          'comparisons':comparisons,'noteReadCalls':reads,
          'compactions':{'count':len(compactions),'firstResponsesAfter':after_compact},
          'explicitContextRemainingCounters':context_counters,
          'gameContextBins':context_bins, 'postCompactionMaterialProxy':dict(post_compaction_counts),
          'selectedErrorContextExamples':error_context_examples,
          'historicalNoteSizes':json.loads((ROOT/'.operator/audits/astra-learning-20261008/assessment.json').read_text())['noteGrowth'],
          'byGame':game_rows,
          'limitations':['No randomisation or controlled replay; prompt size, game stage, procedures and game outcome can affect each other.',
                         'Summary fidelity and loss of useful facts cannot be established from timestamps and lengths; summary text is not inspected.',
                         'A large disk journal is not evidence that its entire contents were loaded into each prompt.',
                         'Input-token totals include all model responses during a game and may include compaction/overhead, not solely move decisions.',
                         'This analysis describes one evolving agent and does not show degradation of model weights.']}
HERE.mkdir(parents=True,exist_ok=True)
(HERE/'context-assessment.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'method':report['method'],'comparisons':comparisons,
                  'compactions':{'count':len(compactions),'earlyAfterInputs':stats([c['nextInputTokens'] for c in after_compact if c['nextBenchmark'] and c['nextBenchmark']<=96]),
                                 'lateAfterInputs':stats([c['nextInputTokens'] for c in after_compact if c['nextBenchmark'] and 103<=c['nextBenchmark']<=198])},
                  'contextBins':context_bins,'postCompactionMaterialProxy':report['postCompactionMaterialProxy'],
                  'selectedErrorContextExamples':error_context_examples,
                  'readToolCalls':len(reads),'unmatchedReadOrCounterCalls':len(pending)},indent=2))
