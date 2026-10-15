#!/usr/bin/env python3
"""Player client: board and move transport only, with stale-position protection."""
from pathlib import Path
import argparse
import json
import os
import urllib.error
import urllib.request
import uuid

def write(path,value):
    tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(value)+'\n');os.chmod(tmp,0o600);tmp.replace(path)
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,required=True)
    sub=parser.add_subparsers(dest='command',required=True)
    for command in ['board','status','start','pgn','export','resign','offer-draw','accept-draw']:
        sub.add_parser(command)
    move=sub.add_parser('move');move.add_argument('uci');move.add_argument('--note',default='')
    note=sub.add_parser('note');note.add_argument('text')
    args=parser.parse_args();root=args.root
    if args.command=='note':
        with (root/'workspace/match-activity.jsonl').open('a') as f:f.write(json.dumps({'note':args.text})+'\n')
        return
    config=json.loads((root/'.match-client.json').read_text())
    def request(path,body=None):
        req=urllib.request.Request(config['origin']+path,data=json.dumps(body).encode() if body else None,
            headers={'Authorization':'Bearer '+config['token'],'Content-Type':'application/json'})
        try:
            with urllib.request.urlopen(req,timeout=20) as r:return json.load(r)
        except urllib.error.HTTPError as e:
            value=json.load(e);print(json.dumps(value));raise SystemExit(1)
        except urllib.error.URLError:
            print('Referee unavailable. The match pauses; retry the same action after recovery.');raise SystemExit(2)
    stamp=root/'.match-position.json';pending=root/'.match-action.json'
    if args.command in ['board','status','start','pgn','export']:
        state=request('/state');write(stamp,{'positionToken':state.get('positionToken')})
        if args.command in ['pgn','export']:
            print(f'[Event "Astra vs Opus — 30-game match"]\n[Round "{state.get("game") or "?"}"]\n[White "{state.get("white") or "?"}"]\n[Black "{state.get("black") or "?"}"]\n[Result "{state.get("result") or "*"}"]\n')
            san=state.get('moves','').split();print(' '.join((str(i//2+1)+'. ' if i%2==0 else '')+s for i,s in enumerate(san)),state.get('result') or '*')
        else:
            board=state.pop('board',None);print(json.dumps(state,indent=2))
            if board:
                for rank,line in zip(range(8,0,-1),board.splitlines()):print(rank,line)
                print('  a b c d e f g h')
        return
    if not stamp.exists():print('Run ./play board first.');raise SystemExit(1)
    action={'command':args.command.replace('-','_'),'positionToken':json.loads(stamp.read_text())['positionToken']}
    if args.command=='move':action.update(uci=args.uci,note=args.note)
    prior=json.loads(pending.read_text()) if pending.exists() else None
    if prior and {k:v for k,v in prior.items() if k!='id'}==action:action=prior
    else:action['id']=str(uuid.uuid4());write(pending,action)
    result=request('/action',action)
    print(json.dumps(result,indent=2))
    # Keep the board stamp at the submitted position until an explicit board read.
    # A transport retry can only replay the same action, never advance a later turn.
    if not result['receipt']['accepted']:raise SystemExit(1)

if __name__=='__main__':main()
