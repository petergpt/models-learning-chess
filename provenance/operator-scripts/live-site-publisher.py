#!/usr/bin/env python3
"""Publish only referee positions/results to the public spectator site."""
from pathlib import Path
import datetime as dt
import fcntl, gzip, hashlib, importlib.util, json, logging, re, time, urllib.request
from functools import lru_cache
ROOT=Path(__file__).resolve().parent.parent
CONFIG=ROOT/'.operator/live-site-publisher-config.json'
STATE=ROOT/'.operator/live-site-publisher-status.json'
THREADS={'astra':'965e6927-c288-4324-b3bb-a1b8b4a16495','opus':'bf1715ee-c265-45bb-9bcf-4b7b6beec6b7'}
EXTRA_CONFIG=ROOT/'.operator/additional-chess-runs.json'
EFFORT_AUDIT=ROOT/'.operator/model-effort-audit.json'

def additional_runs():
 return json.loads(EXTRA_CONFIG.read_text()) if EXTRA_CONFIG.exists() else {}

@lru_cache(maxsize=1)
def observer_payload_module():
 path=ROOT/'Chess - GPT-6-Astra/.arena/dashboard-server/studio.py'
 spec=importlib.util.spec_from_file_location('public_comparison_payload',path)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 return module

@lru_cache(maxsize=1)
def match_referee_module():
 path=ROOT/'.operator/match-referee.py'
 spec=importlib.util.spec_from_file_location('public_match_referee',path)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 return module

def match_payload():
 folder=ROOT/'Matches/Astra vs Opus - 30 games'
 if not (folder/'.referee/match.sqlite').exists():return None
 referee=match_referee_module().Referee(folder)
 return match_spectator_module().enrich(referee,referee.public())

@lru_cache(maxsize=1)
def match_spectator_module():
 path=ROOT/'.operator/match-spectator.py'
 spec=importlib.util.spec_from_file_location('public_match_activity',path)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 return module

def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def pick(value,keys):return {k:value[k] for k in keys if k in value}
def read_runs(page):
 """Read the explicit JSON payload, retaining older dashboard compatibility."""
 embedded=re.search(r'<script\b[^>]*\bid=[\"\']runs-data[\"\'][^>]*>(.*?)</script\s*>',page,re.S|re.I)
 if embedded:
  runs=json.loads(embedded.group(1))
 else:
  assignment=re.search(r'\b(?:const|let|var)\s+RUNS\s*=\s*',page)
  if not assignment:raise ValueError('Dashboard data payload is missing')
  runs=json.JSONDecoder().raw_decode(page[assignment.end():])[0]
 if not isinstance(runs,dict) or not all(isinstance(runs.get(key),dict) for key in THREADS):
  raise ValueError('Dashboard data must contain both model runs')
 return runs
REASONING={}  # model id -> reasoning effort from the learner thread's live model selection
CONTEXT={}    # model id -> context window in tokens, as reported by the provider

def window_tokens(value):
 """'1m' / '200k' style model options to a token count."""
 match=re.fullmatch(r'(\d+(?:\.\d+)?)([km])',str(value).strip().lower())
 return int(float(match.group(1))*(1_000_000 if match.group(2)=='m' else 1_000)) if match else None

def thread_states():
 token=json.loads((ROOT/'.operator/t3-session.json').read_text())['token']
 result={}
 threads={**THREADS,**{id:run['threadId'] for id,run in additional_runs().items()}}
 for id,thread in threads.items():
  try:
   req=urllib.request.Request(f'http://127.0.0.1:3773/api/orchestration/threads/{thread}?turnLimit=1',headers={'Authorization':'Bearer '+token})
   with urllib.request.urlopen(req,timeout=5) as response:t=json.load(response)['thread']
   result[id]=(t.get('session') or {}).get('status','unknown')
   options={o.get('id'):o.get('value') for o in (t.get('modelSelection') or {}).get('options') or [] if isinstance(o,dict)}
   effort=options.get('reasoningEffort',options.get('effort'))
   if isinstance(effort,str) and re.fullmatch(r'[a-z-]{1,20}',effort):REASONING[id]=effort
   updates=[a for a in t.get('activities') or [] if isinstance(a,dict) and a.get('kind')=='context-window.updated']
   window=(max(updates,key=lambda a:a.get('createdAt') or '').get('payload') or {}).get('maxTokens') if updates else None
   window=window if isinstance(window,int) else window_tokens(options.get('contextWindow'))
   if window and 1_000<=window<=100_000_000:CONTEXT[id]=window
  except (OSError,ValueError):result[id]='unknown'
 return result

FOLDERS={'astra':'Chess - GPT-6-Astra','opus':'Chess - Opus-5.5'}  # extra runs name their folder in additional-chess-runs.json

@lru_cache(maxsize=1)
def chess_module():
 import sys
 sys.path.insert(0,str(ROOT/'Chess - GPT-6-Astra/.arena/vendor/chess-1.11.2'))
 import chess
 return chess

def classify(moves,submitted):
 """Why a submitted move was illegal, judged after the fact from the recorded position."""
 chess=chess_module();board=chess.Board()
 try:
  for uci in moves:board.push_uci(uci)
 except ValueError:return 'other'
 try:move=chess.Move.from_uci(submitted)
 except ValueError:return 'notation'
 if board.is_legal(move):return 'other'
 piece=board.piece_at(move.from_square);target=board.piece_at(move.to_square)
 if piece is None:return 'empty_square'
 if piece.color!=board.turn:return 'opponent_piece'
 if target and target.color==board.turn:return 'own_piece'
 if piece.piece_type==chess.KING and abs(chess.square_file(move.from_square)-chess.square_file(move.to_square))==2:return 'castling'
 if piece.piece_type==chess.PAWN and move.promotion is None and chess.square_rank(move.to_square) in (0,7) and board.is_legal(chess.Move(move.from_square,move.to_square,chess.QUEEN)):return 'notation'
 if board.is_pseudo_legal(move):return 'king_in_check'
 lone=chess.Board(None);lone.turn=board.turn;lone.set_piece_at(move.from_square,piece)
 if piece.piece_type==chess.PAWN and chess.square_file(move.from_square)!=chess.square_file(move.to_square) and target:lone.set_piece_at(move.to_square,target)
 promoted=chess.Move(move.from_square,move.to_square,chess.QUEEN)
 return 'blocked' if lone.is_pseudo_legal(move) or (piece.piece_type==chess.PAWN and lone.is_pseudo_legal(promoted)) else 'impossible'

class IllegalMoves:
 """Benchmark illegal-move attempts per game, read incrementally from an append-only ledger."""
 def __init__(self,folder):self.path=folder/'data/ledger.jsonl';self.reset()
 def reset(self):self.offset=0;self.partial=b'';self.moves={};self.attempts={}
 def update(self):
  try:size=self.path.stat().st_size
  except OSError:return self.attempts
  if size<self.offset:self.reset()
  if size==self.offset:return self.attempts
  with self.path.open('rb') as ledger:ledger.seek(self.offset);chunk=self.partial+ledger.read(size-self.offset)
  self.offset=size;lines=chunk.split(b'\n');self.partial=lines.pop()
  for line in lines:
   try:event=json.loads(line)
   except ValueError:continue
   kind,game=event.get('kind'),event.get('game')
   if kind=='start':self.moves[game]=[]
   elif kind=='move' and game in self.moves:self.moves[game].append(str(event.get('uci','')))
   elif kind=='illegal' and game in self.moves:
    submitted=str(event.get('submitted',''))[:12]
    self.attempts.setdefault(game,[]).append([event.get('ply'),submitted,classify(self.moves[game],submitted)])
  return self.attempts

TRACKERS={}
def illegal_attempts(id):
 folder=FOLDERS.get(id) or (additional_runs().get(id) or {}).get('folder')
 if not folder:return {}
 path=(ROOT/folder).resolve()
 if path.parent!=ROOT:return {}
 return TRACKERS.setdefault(path,IllegalMoves(path)).update()

def snapshot(states=None):
 with urllib.request.urlopen('http://127.0.0.1:8765/',timeout=10) as response:html=response.read().decode()
 runs=read_runs(html)
 for id,metadata in additional_runs().items():
  if id in runs:continue
  folder=(ROOT/metadata['folder']).resolve()
  if folder.parent!=ROOT:raise ValueError('Additional learner folder must belong to this project')
  with (folder/'data/.lock').open() as lock:
   fcntl.flock(lock,fcntl.LOCK_SH)
   raw=(folder/'data/dashboard.html').read_text()
  runs[id]=observer_payload_module().build_payload(raw,folder)
  runs[id]['runId']=id;runs[id]['label']=metadata['label']
 audit=json.loads(EFFORT_AUDIT.read_text()).get('runs',{}) if EFFORT_AUDIT.exists() else {}
 safe={}
 for id,d in runs.items():
  run=pick(d,['generated','model','stats','runStarted','displayRatingHistory','ratingBaseline','gameLimit','runId','label'])
  run['rating']=pick(d.get('rating') or {},['estimate','lower','upper','window','rated_games_total','rated_games_in_window','interval_level','interval_type'])
  run['learning']={'trials':[],'practiceSessions':0,'practiceMoves':0}
  run['games']=[];illegal=illegal_attempts(id)
  for g in d['games']:
   entry=pick(g,['id','pgn']);entry['start']=pick(g['start'],['game','color','timestamp'])
   entry['start']['opponent']=pick(g['start']['opponent'],['id','options'])
   entry['moves']=[pick(m,['uci','san','fen','actor']) for m in g['moves']]
   entry['end']=pick(g['end'],['score','result','reason','timestamp','plies']) if g.get('end') else None
   if g['id'] in illegal:entry['illegal']=illegal[g['id']]
   run['games'].append(entry)
  count=sum((g['end'] or {}).get('score') is not None for g in run['games'])
  active=any(not g['end'] for g in run['games'])
  session=(states or {}).get(id,'unknown')
  run['liveState']='complete' if count>=200 else ('playing' if active else 'learning') if session in ['running','starting'] else 'paused' if session in ['error','stopped','ready','idle'] else 'unknown'
  if id in REASONING:run['reasoning']=REASONING[id]
  # A completed run's verified history can differ from its final selector value.
  # Display annotations describe that history; they never configure a learner.
  effort_label=(audit.get(id) or {}).get('displayReasoning')
  if effort_label in ('mixed',):run['reasoning']=effort_label
  if id in CONTEXT:run['contextWindow']=CONTEXT[id]
  safe[id]=run
 match=match_payload()
 public={'runs':safe,'match':match}
 stamp=now();revision=hashlib.sha256(json.dumps(public,sort_keys=True).encode()).hexdigest()+':'+str(int(time.time())//20)
 return {**public,'updatedAt':stamp,'revision':revision}

def publish(config,value):
 body=gzip.compress(json.dumps(value,separators=(',',':')).encode())
 req=urllib.request.Request(config['url'].rstrip('/')+'/api/ingest',data=body,method='PUT',headers={'Authorization':'Bearer '+config['token'],'Content-Type':'application/json','Content-Encoding':'gzip','User-Agent':'Mozilla/5.0'})
 with urllib.request.urlopen(req,timeout=25) as response:result=json.load(response)
 if not result.get('ok') or result.get('revision')!=value['revision']:raise ValueError('Publisher acknowledgment mismatch')
 return result

def write_state(state):
 temp=STATE.with_suffix('.json.tmp');temp.write_text(json.dumps(state,indent=2)+'\n');temp.replace(STATE)

def main():
 config=json.loads(CONFIG.read_text());last=None;states={};next_states=0;last_success=None
 while True:
  start=time.monotonic()
  try:
   if start>=next_states:states=thread_states();next_states=start+20
   value=snapshot(states)
   if value['revision']!=last:
    result=publish(config,value);last=value['revision'];last_success=now()
    write_state({'status':'syncing','lastSuccess':last_success,'revision':last,'models':{id:{'status':r['liveState'],'games':sum((g['end'] or {}).get('score') is not None for g in r['games']),'elo':r['rating']['estimate']} for id,r in value['runs'].items()}})
  except Exception as error:
   logging.warning('Dashboard publish failed: %s',type(error).__name__)
   write_state({'status':'retrying','lastSuccess':last_success,'error':type(error).__name__})
  time.sleep(max(1,5-(time.monotonic()-start)))
if __name__=='__main__':
 logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s');main()
