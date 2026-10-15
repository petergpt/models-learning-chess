from load import *
import importlib.util
spec = importlib.util.spec_from_file_location('rating', ROOT/'Chess - GPT-6-Astra/.arena/rating.py')
rating = importlib.util.module_from_spec(spec); spec.loader.exec_module(rating)

def per_game(key):
    folder, ev, g, other, pev, pg, pother = load(key)
    rows=[]
    prev_end=None
    pstarts=[(ts(p['start']['timestamp']), p) for p in pg.values()]
    for n,x in g.items():
        s=x['start']; e=x['end']
        if not e or e['score'] is None: continue
        learner_white = s['color']=='white'
        secs=[m['seconds'] for m in x['moves'] if m['actor']=='model' and isinstance(m.get('seconds'),(int,float))]
        st=ts(s['timestamp']); en=ts(e['timestamp'])
        gap=(st-prev_end).total_seconds()/3600 if prev_end else None
        npr=sum(1 for t,p in pstarts if prev_end and prev_end<=t<=st) if prev_end else sum(1 for t,p in pstarts if t<=st)
        rows.append(dict(game=n, opp=s['opponent']['id'], color=s['color'], score=e['score'], reason=e['reason'],
            plies=e['plies'], ownmoves=len(secs), ill=len(x['illegal']), start=st, end=en,
            dur_h=(en-st).total_seconds()/3600, think_s=sum(secs), med_s=statistics.median(secs) if secs else None,
            gap_h=gap, practice_before=npr, snapshot=s.get('snapshot')))
        prev_end=en
    return rows

def elo(rows):
    obs=[dict(anchor=rating.ANCHORS[r['opp']], score=r['score']) for r in rows if r['opp'] in rating.ANCHORS]
    if not obs: return None
    p=rating.posterior(obs); return p['estimate'],p['lower'],p['upper'],len(obs)

def fmt(rows):
    def sc(rs): 
        return f"{sum(r['score'] for r in rs):.1f}/{len(rs)}" if rs else '-'
    return sc
if __name__=='__main__':
    import sys
    key=sys.argv[1]
    rows=per_game(key)
    for r in rows:
        print(f"{r['game']:3d} {r['opp'][:5]:5s} {r['color'][0]} {r['score']:.1f} {r['reason'][:12]:12s} plies={r['plies']:3d} ill={r['ill']} dur={r['dur_h']:.2f}h med={r['med_s'] or 0:.0f}s think={r['think_s']/60:.0f}m gap={(r['gap_h'] or 0):.2f}h prac={r['practice_before']} {r['start']:%m-%d %H:%M}")
