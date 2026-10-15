from table import *
import sys
B=int(sys.argv[1]) if len(sys.argv)>1 else 30
for key in RUNS:
    rows=per_game(key)
    print(f'== {key}  (blocks of {B} games)')
    for i in range(0, len(rows), B):
        blk=rows[i:i+B]
        def s(op):
            r=[x for x in blk if x['opp']==op]; return f"{sum(x['score'] for x in r):4.1f}/{len(r):2d}"
        e=elo(blk) or (None,None,None,0)
        med=statistics.median([x['med_s'] for x in blk if x['med_s']])
        think=statistics.mean([x['think_s']/60 for x in blk])
        prac=sum(x['practice_before'] for x in blk)
        ill=sum(x['ill'] for x in blk); own=sum(x['ownmoves'] for x in blk)
        print(f"  g{blk[0]['game']:3d}-{blk[-1]['game']:3d}  full {s('full-strength')}  sk0 {s('skill-0')}  1800 {s('elo-1800-setting')}  Elo(window) {e[0]}[{e[1]}-{e[2]}] n={e[3]}  med_move_s={med:4.0f} think/game={think:4.0f}m  practice={prac:2d}  illegal/100={100*ill/own:.2f}")
