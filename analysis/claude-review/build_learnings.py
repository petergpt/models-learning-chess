#!/usr/bin/env python3
"""Build the "How the models learned" page (deliverables/chess-learnings.html).

Read-only on learner folders. Inputs: benchmark/practice ledgers, workspace snapshots,
learner notes (hand-coded trial schedules below, with sources), and the cached post-hoc
Stockfish evaluations in evals/ (run engine_review.py first for new games).
"""
import collections, datetime as dt, importlib.util, json, re, statistics, sys, tarfile, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from load import RUNS, load, ts                      # noqa: E402
from table import per_game                          # noqa: E402
from quality import load_run, wp                    # noqa: E402

spec = importlib.util.spec_from_file_location('rating', ROOT / 'Chess - GPT-6-Astra/.arena/rating.py')
rating = importlib.util.module_from_spec(spec); spec.loader.exec_module(rating)

ORDER = ['astra', 'opus', 'sol', 'solLC', 'fable']
META = {
    'astra': dict(name='Astra', full='GPT-6 Astra', maker='OpenAI', logo='logo-openai', color='#4a8ee8'),
    'opus': dict(name='Opus 5.5', full='Claude Opus 5.5', maker='Anthropic', logo='logo-claude', color='#d77352'),
    'sol': dict(name='Sol', full='GPT-6.1 Sol', maker='OpenAI', logo='logo-openai', color='#10a37f'),
    'solLC': dict(name='Sol · Long Context', full='GPT-6.1 Sol · Long Context', maker='OpenAI', logo='logo-openai', color='#e47bc4'),
    'fable': dict(name='Fable 5.1', full='Claude Fable 5.1', maker='Anthropic', logo='logo-claude', color='#dcae46'),
}
LIVE_IDS = {'astra': 'astra', 'opus': 'opus', 'sol': 'sol', 'solLC': 'sol-long-context', 'fable': 'fable'}
CONTEXT_FALLBACK = {'astra': 258400, 'opus': 1000000, 'sol': 258400, 'solLC': 828400, 'fable': 1000000}
ANCH = rating.ANCHORS

# --- Learning-method schedules (from the learners' own notes) -------------------------
# Opus: PLAN.md trials T0..Tn, each covering six games starting at 1 + 6n.
# Astra: learning-journal.md trials T01..T29 at games 31 + 6(k-1) (no trials before the goal change).
# Sol: journal.md declares a trial before every benchmark (39 trials by game 33).
# Sol · LC: learning.md trials 1-13 before games 2-13; trial 13 drops drills ("repeated drill success
#   has not supplied fresh transfer") and no further trial is declared through game 18.
# Fable: procedure.md is revised before almost every game (detected from snapshots below).
STYLE = {
    'astra': 'New focus every 6 games',
    'opus': 'Review, then add a rule',
    'sol': 'Tiny drill after every game',
    'solLC': 'Drills, then none',
    'fable': 'Patch the checklist',
}
PHASES = [  # Astra's instruction changes (ledger events seq 2551, 5512, 10705)
    dict(game=30, label='Learning trials required'),
    dict(game=66, label='Practice tool added'),
    dict(game=131, label='200-game cap set'),
]


def elo_of(rows):
    obs = [dict(anchor=ANCH[r['opp']], score=r['score']) for r in rows if r['opp'] in ANCH]
    if not obs:
        return None
    p = rating.posterior(obs)
    return dict(est=p['estimate'], lo=p['lower'], hi=p['upper'], n=len(obs))


def elo_history(key):
    folder, ev, g, other, *_ = load(key)
    games = [dict(start=x['start'], end=x['end']) for x in g.values()]
    hist = rating.estimate(games, cache_path=None)['history']
    return [[p['game'], p['estimate'], p['lower'], p['upper'], p['rated_games']] for p in hist]


def move_seconds(key):
    folder, ev, g, other, *_ = load(key)
    out = collections.defaultdict(list)
    for n, x in g.items():
        for m in x['moves']:
            if m['actor'] == 'model' and isinstance(m.get('seconds'), (int, float)):
                out[n].append(m['seconds'])
    return out


def blunders(evals, games):
    n = b = 0
    for gnum in games:
        d = evals.get(gnum)
        if not d:
            continue
        for m in d['moves']:
            if m['actor'] == 'model':
                n += 1
                b += (wp(m['before']) - wp(m['after'])) >= 30
    return (100 * b / n if n else None), n


def snapshot_sizes(key, filename):
    folder, ev, g, *_ = load(key)
    cache, out = {}, []
    for n, x in g.items():
        h = x['start'].get('snapshot')
        if h not in cache:
            with tarfile.open(folder / 'data/snapshots' / (h + '.tar.gz'), 'r:gz') as t:
                names = [m for m in t.getnames() if m == filename or m.endswith('/' + filename)]
                cache[h] = t.getmember(names[0]).size if names else 0
        out.append([n, cache[h]])
    return out


def opus_rule_text():
    """Bytes of per-move rule text in force, from PLAN.md trial definitions.

    From T9 (square scan) every trial kept the previous checks ("keep T9 scans", "T13 plus", ...)
    until T29 replaced the list with four steps; T30/T31 add to T29 again. Observable/result text excluded.
    """
    text = (ROOT / 'Chess - Opus-5.5/workspace/PLAN.md').read_text().splitlines()
    defs, cur = {}, None
    for line in text:
        m = re.match(r'- T(\d+) \(games (\d+)-(\d+)\):(.*)', line)
        if m:
            cur = int(m.group(1)); defs[cur] = dict(start=int(m.group(2)), text=m.group(4))
            continue
        if line.startswith('- ') or 'RESULT' in line or re.match(r'\s+(after|Elo|Rated|Zero|rated|Target|Score)', line):
            cur = None
            continue
        if cur is not None:
            defs[cur]['text'] += ' ' + line.strip()
    out, total = [], 0
    for k in sorted(defs):
        if k < 9:
            continue
        body = re.split(r'Observable:', defs[k]['text'])[0].strip()
        total = len(body) if k in (9, 29) else total + len(body)
        out.append([defs[k]['start'], total])
    return out


def practice_points(key):
    folder, ev, g, other, pev, pg, pother = load(key)
    ends = sorted(ts(x['end']['timestamp']) for x in g.values() if x['end'] and x['end']['score'] is not None)
    pts = []
    for x in pg.values():
        t0 = ts(x['start']['timestamp'])
        before = sum(e <= t0 for e in ends)
        own = sum(m['actor'] == 'model' for m in x['moves'])
        opp = x['start'].get('opponent', {}).get('id', '').replace('practice-', '')
        res = (x['end'] or {}).get('reason')
        pts.append([before + 0.5, own, opp, res])
    return pts


def trial_ticks(key, games_played, fable_sizes):
    if key == 'opus':
        return list(range(1, games_played + 1, 6))
    if key == 'astra':
        return list(range(31, min(games_played, 200) + 1, 6))
    if key == 'sol':
        return list(range(1, games_played + 1))
    if key == 'solLC':
        return [g for g in range(2, 14) if g <= games_played]
    if key == 'fable':
        return [g for (g, s), (_, p) in zip(fable_sizes[1:], fable_sizes[:-1]) if s != p]
    return []


def live_context():
    try:
        with urllib.request.urlopen('http://127.0.0.1:8773/data', timeout=8) as r:
            runs = json.load(r)['runs']
        return {k: runs[LIVE_IDS[k]].get('contextWindow') for k in ORDER if LIVE_IDS[k] in runs}
    except Exception:
        return {}


def status_of(key, games):
    if games >= 200:
        return 'done'
    if key == 'fable':
        st = json.loads((ROOT / '.operator/fable-goal.json').read_text()).get('status')
        return 'paused' if st == 'paused' else 'live'
    return 'live'


def main():
    ctx = live_context()
    models, elo_series, quarters, method, where = [], {}, {}, {}, {}
    buckets = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 60), (61, 999)]
    fable_sizes = snapshot_sizes('fable', 'procedure.md')
    for key in ORDER:
        rows = per_game(key)
        games = len(rows)
        evals = load_run(key)
        secs = move_seconds(key)
        hist = elo_history(key)
        last = hist[-1] if hist else None
        m = dict(id=key, **META[key], games=games, status=status_of(key, games),
                 context=ctx.get(key) or CONTEXT_FALLBACK[key], style=STYLE[key],
                 elo=dict(est=last[1], lo=last[2], hi=last[3], rated=last[4]) if last else None, change=None)
        if games >= 120:
            first, recent = rows[:60], rows[-60:]
            a, b = elo_of(first), elo_of(recent)
            m['change'] = dict(fromGames=[first[0]['game'], first[-1]['game']], toGames=[recent[0]['game'], recent[-1]['game']],
                               before=a, after=b, delta=b['est'] - a['est'])
        models.append(m)
        elo_series[key] = hist

        if key in ('astra', 'opus'):
            qs = []
            for lo, hi in ((1, 50), (51, 100), (101, 150), (151, 200)):
                q = [r for r in rows if lo <= r['game'] <= hi]
                if not q:
                    continue
                rated = [r['game'] for r in q if r['opp'] != 'full-strength']
                bl, n = blunders(evals, rated)
                s = [x for gm in rated for x in secs.get(gm, [])]
                qs.append(dict(lo=lo, hi=q[-1]['game'], partial=q[-1]['game'] < hi, elo=elo_of(q),
                               blunders=round(bl, 2) if bl is not None else None, moves=n,
                               analysed=sum(1 for gm in rated if gm in evals), ratedGames=len(rated),
                               seconds=round(statistics.median(s), 1) if s else None))
            quarters[key] = qs

        rules = None
        if key == 'astra':
            rules = dict(unit='bytes', file='move-check.md', points=snapshot_sizes('astra', 'move-check.md'))
        elif key == 'fable':
            rules = dict(unit='bytes', file='procedure.md', points=fable_sizes)
        elif key == 'opus':
            rules = dict(unit='bytes', file='PLAN.md trial rules', points=opus_rule_text())
        prac = practice_points(key)
        method[key] = dict(trials=trial_ticks(key, games, fable_sizes), practice=prac, rules=rules,
                           trialCount={'astra': 29, 'opus': len(range(1, games + 1, 6)), 'sol': None, 'solLC': 13, 'fable': None}[key],
                           practiceMoves=sum(p[1] for p in prac), gameMoves=sum(r['ownmoves'] for r in rows))

        rated_games = [r['game'] for r in rows if r['opp'] != 'full-strength']
        cells = []
        for lo, hi in buckets:
            n = b = 0
            for gm in rated_games:
                d = evals.get(gm)
                if not d:
                    continue
                own = [mv for mv in d['moves'] if mv['actor'] == 'model']
                for i, mv in enumerate(own, 1):
                    if lo <= i <= hi:
                        n += 1
                        b += (wp(mv['before']) - wp(mv['after'])) >= 30
            cells.append([round(100 * b / n, 2) if n else None, n])
        where[key] = cells

    # Sol trial count from its journal headings.
    sol_text = (ROOT / 'Chess - GPT-6.1-Sol/workspace/journal.md').read_text()
    nums = [int(x) for x in re.findall(r'\b[Tt]rial (\d+)', sol_text)]
    method['sol']['trialCount'] = max(nums) if nums else None
    method['fable']['trialCount'] = len(method['fable']['trials'])

    data = dict(generated=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
                models=models, elo=elo_series, phases=PHASES, quarters=quarters, method=method,
                where=dict(buckets=['1–10', '11–20', '21–30', '31–40', '41–60', '61+'], rows=where),
                setup={
                    'astra': [['flag', 'Goal changed 3×'], ['clock', 'Cut its own thinking time']],
                    'opus': [['gauge', 'Treated token counter as a budget'], ['resume', 'Resumed by operator 2×']],
                    'sol': [],
                    'solLC': [['memory', 'Same model as Sol, 3× memory']],
                    'fable': [['pause', 'Paused by user'], ['bolt', 'Rushed moves after status nudges']],
                })
    site = (ROOT / 'surge-site/template.html').read_text()
    font = re.search(r'@font-face\{.*?\}', site, flags=re.S).group(0)
    logos = ''.join(re.search(r'<symbol id="%s".*?</symbol>' % s, site, flags=re.S).group(0) for s in ('logo-openai', 'logo-claude'))
    page = (HERE / 'learnings-template.html').read_text()
    encoded = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    for marker, value in (('/*__FONT__*/', font), ('<!--__LOGOS__-->', logos), ('__DATA__', encoded)):
        assert page.count(marker) == 1, marker
        page = page.replace(marker, value)
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'deliverables/chess-learnings.html'
    tmp = out.with_suffix('.tmp')
    tmp.write_text(page)
    tmp.replace(out)
    (HERE / 'learnings-data.json').write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print(out, len(page))


if __name__ == '__main__':
    main()
