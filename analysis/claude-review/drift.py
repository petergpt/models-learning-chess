import numpy as np
from table import per_game
from load import RUNS
ANCH={'skill-0':1320,'elo-1800-setting':1800}
def drift(rows, lo=None, hi=None):
    rs=[r for r in rows if r['opp'] in ANCH and (lo is None or r['game']>=lo) and (hi is None or r['game']<=hi)]
    g=np.array([r['game'] for r in rs],float); c=g.mean()
    x=(g-c)/100.0
    anc=np.array([ANCH[r['opp']] for r in rs],float); s=np.array([r['score'] for r in rs])
    A=np.arange(800,2600,10.)[:,None,None]; B=np.arange(-800,801,10.)[None,:,None]
    D=((np.arange(40)+.5)/40)[None,None,:]; lognu=np.log(2*D/(1-D))
    ll=np.zeros((A.shape[0],B.shape[1],D.shape[2]))
    for xi,ai,si in zip(x,anc,s):
        m=np.log(10)*((A+B*xi)-ai)/800
        den=np.logaddexp(np.logaddexp(m,-m),lognu)
        ll+= (m-den) if si==1 else ((-m-den) if si==0 else (lognu-den))
    prior=-.5*((A-1500)/800)**2
    lp=ll+prior
    lp-=lp.max(); p=np.exp(lp); p/=p.sum()
    pb=p.sum(axis=(0,2)); bs=B[0,:,0]
    cdf=np.cumsum(pb)
    q=lambda v: bs[np.searchsorted(cdf,v)]
    pa=p.sum(axis=(1,2)); ca=np.cumsum(pa); As=A[:,0,0]
    return dict(n=len(rs), center=c, slope_med=q(.5), lo=q(.025), hi=q(.975), p_pos=float(pb[bs>0].sum()),
                level=As[np.searchsorted(ca,.5)])
if __name__=='__main__':
    for k in RUNS:
        rows=per_game(k)
        d=drift(rows)
        print(f"{k:6s} rated n={d['n']:3d}  slope {d['slope_med']:+5.0f} Elo/100 games  95% [{d['lo']:+.0f}, {d['hi']:+.0f}]  P(slope>0)={d['p_pos']:.2f}  level at game {d['center']:.0f}: {d['level']:.0f}")
    rows=per_game('astra')
    for lo,hi in ((1,66),(31,200),(67,200),(1,120),(121,200)):
        d=drift(rows,lo,hi); print(f"  astra g{lo}-{hi}: slope {d['slope_med']:+.0f} [{d['lo']:+.0f},{d['hi']:+.0f}] P>0={d['p_pos']:.2f}")
    rows=per_game('opus')
    for lo,hi in ((1,60),(1,120),(55,200),(91,200),(121,200)):
        d=drift(rows,lo,hi); print(f"  opus g{lo}-{hi}: slope {d['slope_med']:+.0f} [{d['lo']:+.0f},{d['hi']:+.0f}] P>0={d['p_pos']:.2f}")
