"""Mechanical replay only: explicitly chosen own-study lines; no search/evaluation."""
import sys,gzip,json
from pathlib import Path
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path.cwd()/'.arena/vendor/chess-1.11.2'))
import chess,chess.pgn
cases=[
 (166,51,['d3d6','e6f5','h7g8']),
 (167,46,['f1f2','c4e2','d1d2']),
 (168,59,['g4f6','h4h6','h7g7']),
 (168,77,['d2d8','g6g7','d8g8'])
]
out=[]
for n,ply,line in cases:
 with gzip.open(f'data/games/{n:06}.pgn.gz','rt') as f:g=chess.pgn.read_game(f)
 b=g.board()
 for i,m in enumerate(g.mainline_moves()):
  if i==ply:break
  b.push(m)
 r={'game':n,'ply':ply,'start':b.fen(),'line':[]}
 for u in line:
  m=chess.Move.from_uci(u)
  valid=b.is_legal(m)
  r['line'].append({'uci':u,'legal':valid})
  if not valid:break
  b.push(m)
 r['end']=b.fen()
 out.append(r)
Path('workspace/trials/destination-checks-24-legality.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
