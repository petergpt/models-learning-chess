import json, math, statistics, collections, sys
from pathlib import Path
sys.path.insert(0,'/home/peter/Chess Learning/.operator/claude-review')
from table import per_game
from load import RUNS
EV=Path('/home/peter/Chess Learning/.operator/claude-review/evals')
def wp(cp):
    cp=max(-1500,min(1500,cp))
    return 50+50*(2/(1+math.exp(-0.00368208*cp))-1)
def game_stats(d):
    mv=[m for m in d['moves'] if m['actor']=='model']
    out=dict(n=len(mv), cpl=[], drops=[], blunders=0, mistakes=0, inacc=0, acc=[], first_bad_ply=None, max_eval=-99999, best_matches=0)
    for m in mv:
        b=max(-1000,min(1000,m['before'])); a=max(-1000,min(1000,m['after']))
        out['cpl'].append(max(0,b-a))
        drop=wp(m['before'])-wp(m['after'])
        out['drops'].append(drop)
        if drop>=30: out['blunders']+=1
        elif drop>=20: out['mistakes']+=1
        elif drop>=10: out['inacc']+=1
        out['acc'].append(max(0,min(100,103.1668*math.exp(-0.04354*max(0,drop))-3.1669)))
        if m['best']==m['uci']: out['best_matches']+=1
        if drop>=30 and out['first_bad_ply'] is None: out['first_bad_ply']=m['ply']
    for m in d['moves']:
        if m['actor']=='sf':  # eval after sf move from model's perspective = -(sf's 'after')
            out['max_eval']=max(out['max_eval'], -m['after'])
    return out
def load_run(k):
    res={}
    for p in EV.glob(f'{k}-*.json'):
        d=json.loads(p.read_text()); res[d['game']]=d
    return res
if __name__=='__main__':
    B=int(sys.argv[1]) if len(sys.argv)>1 else 30
    for k in RUNS:
        rows={r['game']:r for r in per_game(k)}
        ev=load_run(k)
        games=sorted(g for g in ev if g in rows)
        if not games: continue
        print(f'== {k} ({len(games)} games analysed)')
        for i in range(0,len(games),B):
            blk=games[i:i+B]
            S=[game_stats(ev[g]) for g in blk]
            n=sum(s['n'] for s in S)
            bl=sum(s['blunders'] for s in S); mi=sum(s['mistakes'] for s in S)
            acpl=statistics.mean([c for s in S for c in s['cpl']])
            acc=statistics.mean([a for s in S for a in s['acc']])
            # rated-only blunders
            Sr=[game_stats(ev[g]) for g in blk if rows[g]['opp']!='full-strength']
            nr=sum(s['n'] for s in Sr); blr=sum(s['blunders'] for s in Sr)
            gw=[g for g in blk if rows[g]['opp']!='full-strength' and game_stats(ev[g])['max_eval']>=300]
            conv=sum(rows[g]['score']==1 for g in gw)
            print(f"  g{blk[0]:3d}-{blk[-1]:3d}: moves {n:5d}  ACPL {acpl:5.1f}  accuracy {acc:4.1f}%  blunders/100 {100*bl/n:4.2f} (rated {100*blr/max(1,nr):4.2f})  mistakes/100 {100*mi/n:4.2f}  rated games reaching +3: {len(gw):2d}, won {conv}")
