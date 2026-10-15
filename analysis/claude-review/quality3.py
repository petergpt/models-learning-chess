from quality import *
from load import load
def per_move_time(k):
    folder, ev, g, other, pev, pg, pother = load(k)
    t={}
    for n,x in g.items():
        for m in x['moves']:
            if m['actor']=='model': t[(n,m['ply'])]=m.get('seconds')
    return t
for k in ('astra','opus','sol'):
    rows={r['game']:r for r in per_game(k)}; ev=load_run(k); T=per_move_time(k)
    buckets=collections.defaultdict(lambda:[0,0,0.0])
    phase=collections.defaultdict(lambda:[0,0,0.0])
    for gnum,d in ev.items():
        if rows.get(gnum,{}).get('opp') in (None,'full-strength'): continue
        own=0
        for m in d['moves']:
            if m['actor']!='model': continue
            own+=1
            s=T.get((gnum,m['ply']))
            if s is None: continue
            drop=wp(m['before'])-wp(m['after'])
            b='<10s' if s<10 else '10-30s' if s<30 else '30-90s' if s<90 else '>90s'
            buckets[b][0]+=1; buckets[b][1]+= drop>=30; buckets[b][2]+=max(0,min(1000,m['before'])-min(1000,max(-1000,m['after'])))
            ph='moves 1-12' if own<=12 else 'moves 13-30' if own<=30 else 'moves 31+'
            phase[ph][0]+=1; phase[ph][1]+=drop>=30; phase[ph][2]+=max(0,min(1000,m['before'])-min(1000,max(-1000,m['after'])))
    print('==',k,'(rated games) blunders/100 by time spent on the move:', {b:f"{100*v[1]/v[0]:.2f} (n={v[0]})" for b,v in sorted(buckets.items())})
    print('   by game phase:', {b:f"{100*v[1]/v[0]:.2f}/100, ACPL {v[2]/v[0]:.0f} (n={v[0]})" for b,v in sorted(phase.items())})
# opening-phase ACPL over time
print()
for k in ('astra','opus'):
    rows={r['game']:r for r in per_game(k)}; ev=load_run(k)
    out=[]
    for lo in range(1,200,30):
        c=[];bl=0;n=0
        for gnum in range(lo,lo+30):
            d=ev.get(gnum)
            if not d or rows[gnum]['opp']=='full-strength': continue
            own=[m for m in d['moves'] if m['actor']=='model']
            for i,m in enumerate(own):
                ph = i<12
                if not ph: continue
                c.append(max(0,min(1000,m['before'])-min(1000,max(-1000,m['after']))))
                bl+= (wp(m['before'])-wp(m['after']))>=30; n+=1
        if n: out.append(f"g{lo}-{lo+29}: {statistics.mean(c):.0f} cpl, {100*bl/n:.1f} bl/100")
    print(k,'opening (first 12 own moves, rated):',' | '.join(out))
