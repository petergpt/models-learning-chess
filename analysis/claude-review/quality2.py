from quality import *
def agg(ev, games, rows, opp=None):
    S=[game_stats(ev[g]) for g in games if g in ev and (opp is None or (rows[g]['opp']!='full-strength' if opp=='rated' else rows[g]['opp']==opp))]
    n=sum(s['n'] for s in S)
    if not n: return None
    return dict(games=len(S), n=n, acpl=statistics.mean([c for s in S for c in s['cpl']]),
                bl=100*sum(s['blunders'] for s in S)/n, mi=100*sum(s['mistakes'] for s in S)/n,
                acc=statistics.mean([a for s in S for a in s['acc']]))
def fmt(a): return '-' if not a else f"ACPL {a['acpl']:5.1f} blunders/100 {a['bl']:4.2f} mistakes/100 {a['mi']:4.2f} acc {a['acc']:4.1f}% ({a['games']}g/{a['n']}mv)"
print('EQUAL FOOTING: first 15 games, by opponent')
for k in RUNS:
    rows={r['game']:r for r in per_game(k)}; ev=load_run(k)
    G=[g for g in sorted(ev) if g<=15 and g in rows]
    print(f"  {k:6s} all: {fmt(agg(ev,G,rows))}")
    print(f"         rated: {fmt(agg(ev,G,rows,'rated'))}")
    print(f"         full:  {fmt(agg(ev,G,rows,'full-strength'))}")
print('\nFirst 32 games (astra/opus/sol)')
for k in ('astra','opus','sol'):
    rows={r['game']:r for r in per_game(k)}; ev=load_run(k)
    G=[g for g in sorted(ev) if g<=32 and g in rows]
    print(f"  {k:6s} rated: {fmt(agg(ev,G,rows,'rated'))}")
print('\nASTRA by instruction phase (rated games only)')
rows={r['game']:r for r in per_game('astra')}; ev=load_run('astra')
for name,lo,hi in (('A g1-30',1,30),('B g31-66',31,66),('C g67-132',67,132),('D g133-200',133,200)):
    G=[g for g in sorted(ev) if lo<=g<=hi]
    print(f"  {name:11s} rated: {fmt(agg(ev,G,rows,'rated'))}")
    print(f"  {'':11s} full : {fmt(agg(ev,G,rows,'full-strength'))}")
print('\nOPUS by 60 games (rated / full)')
rows={r['game']:r for r in per_game('opus')}; ev=load_run('opus')
for lo,hi in ((1,60),(61,120),(121,184),(121,150),(151,184)):
    G=[g for g in sorted(ev) if lo<=g<=hi]
    print(f"  g{lo}-{hi} rated: {fmt(agg(ev,G,rows,'rated'))}")
    print(f"  {'':8s} full : {fmt(agg(ev,G,rows,'full-strength'))}")
