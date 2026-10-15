#!/usr/bin/env python3
"""Relay public match turns to the two native T3 player branches, always at Max."""
from pathlib import Path
import argparse
import datetime as dt
import fcntl
import hashlib
import importlib.util
import json
import logging
import re
import time
import urllib.request
import uuid

ROOT=Path(__file__).resolve().parent.parent
MATCH=ROOT/'Matches/Astra vs Opus - 30 games'
SETUP=MATCH/'.operator/setup.json'
STATE=MATCH/'.operator/controller.json'
spec=importlib.util.spec_from_file_location('match_referee',ROOT/'.operator/match-referee.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def save(state):
    state['updatedAt']=now();temp=STATE.with_suffix('.tmp');temp.write_text(json.dumps(state,indent=2)+'\n');temp.replace(STATE)
def request(path,command=None):
    token=json.loads((ROOT/'.operator/t3-session.json').read_text())['token']
    req=urllib.request.Request('http://127.0.0.1:3773'+path,
        data=json.dumps(command).encode() if command else None,
        headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=25) as r:return json.load(r)

class Controller:
    def __init__(self):
        self.setup=json.loads(SETUP.read_text());self.players=self.setup['players'];self.ref=module.Referee()
        self.state=json.loads(STATE.read_text()) if STATE.exists() else {'status':'prepared','slots':{},'ownMessageIds':[],'createdAt':now(),'dispatches':0}
        save(self.state)
    def snapshot(self,id):return request('/api/orchestration/threads/'+self.players[id]['threadId']+'?turnLimit=1')['thread']
    @staticmethod
    def idle(thread):
        return (thread.get('session') or {}).get('status') not in ('running','starting') and (thread.get('latestTurn') or {}).get('state') not in ('running','starting','pending')
    def stopped(self,thread):
        if thread.get('deletedAt') or thread.get('archivedAt') or thread.get('snoozedUntil') or thread.get('settledOverride'):return True
        if (thread.get('latestTurn') or {}).get('state')=='interrupted':return True
        for m in thread.get('messages',[]):
            if m.get('role')=='user' and m['id'] not in self.state['ownMessageIds'] and re.search(r'\b(?:pause|cancel|stop (?:now|this|the match|playing)|do not continue|don.t continue)\b',m.get('text',''),re.I):return True
        return False
    def status(self,value,reason=None):
        self.state['status']=value;self.state['reason']=reason;save(self.state)
        with self.ref.connect() as db:
            current=self.ref.meta(db,'status')
            if value in ['paused','waiting'] and current not in ['complete','unfinished']:
                self.ref.set_meta(db,'status',value)
                self.ref.event(db,'infrastructure_pause' if value=='waiting' else 'operator_pause',self.ref._state(db)['game'],None,{'reason':reason})
    def activate(self):
        """Release an infrastructure wait before asking the player to act."""
        with self.ref.connect() as db:
            if self.ref.meta(db,'status')=='waiting':
                game=self.ref.current(db)
                self.ref.set_meta(db,'status','playing' if game and not game['ended'] else 'between_games')
                position=self.ref._state(db)
                self.ref.event(db,'infrastructure_resume',position['game'],None,
                    {'reason':'Controller resumed the unchanged position after an infrastructure pause.','ply':position.get('ply')})
        self.status('active')
    def dispatch(self,player,slot,text,thread):
        record=self.state['slots'].get(slot)
        if record:
            own=any(m['id']==record['command']['message']['messageId'] for m in thread.get('messages',[]))
            if record.get('acknowledged') or own:
                record['acknowledged']=True;save(self.state)
                return record
        else:
            message_id=str(uuid.uuid4())
            command={'type':'thread.turn.start','commandId':str(uuid.uuid4()),'threadId':self.players[player]['threadId'],
                'modelSelection':self.players[player]['modelSelection'],
                'message':{'messageId':message_id,'role':'user','text':text,'attachments':[]},
                'runtimeMode':'full-access','interactionMode':'default','createdAt':now()}
            record={'player':player,'command':command,'acknowledged':False,'createdAt':now()}
            self.state['slots'][slot]=record;self.state['ownMessageIds'].append(message_id);save(self.state)
        # The same commandId and exact body survive an uncertain network response.
        request('/api/orchestration/dispatch',record['command'])
        record['acknowledged']=True;self.state['dispatches']+=1;save(self.state)
        logging.info('Dispatched %s to %s',slot,player)
        return record
    def completed(self,record,thread):
        if not record:return False
        turn=thread.get('latestTurn') or {}
        return turn.get('state')=='completed' and self.idle(thread) and any(m['id']==record['command']['message']['messageId'] for m in thread.get('messages',[]))
    def prepare(self):
        for id,p in self.players.items():
            thread=self.snapshot(id)
            if not self.idle(thread):continue
            self.dispatch(id,'prepare:'+id,
                'The user has authorized a formal 30-game Astra–Opus match, starting from your completed 200-game learner. '
                'This is a genuine native conversation fork with your own final workspace copied into '+p['folder']+'. '
                'The original run remains complete and untouched. The new AGENTS.md, CLAUDE.md, GOAL.md and MATCH-RULES.md apply to this branch. '
                'For this preparation turn only, read those local instructions and your own retained notes as needed. '
                'Confirm readiness briefly, without making any move, starting any old benchmark, external study, polling, or reading any other folder. '
                'The neutral referee is installed; game one starts after both players have finished this preparation and settings have been verified. '
                'All playing and reflection turns will explicitly use Max reasoning. End this turn once ready.',thread)
        self.status('preparing')
    def retry(self,id,key,text,thread):
        record=self.state['slots'].get(key)
        if not record:
            self.activate()
            return self.dispatch(id,key,text,thread)
        if not self.idle(thread):return
        turn=thread.get('latestTurn') or {};session=thread.get('session') or {}
        if turn.get('state') in ('error','failed') or session.get('status')=='error':
            n=record.setdefault('retryCount',0)
            if 'retryAt' not in record:
                record['retryAt']=time.time()+min(900,60*(2**min(n,4)));save(self.state)
                self.status('waiting','Provider request failed; same position retained, retrying with backoff.')
            if time.time()<record['retryAt']:return
            retry_key=key+':retry:'+str(n+1)
            self.activate()
            result=self.dispatch(id,retry_key,text+' The prior provider request failed; continue the unchanged position. No chess points were awarded for that failure.',thread)
            # Continue observing the newest attempt under the same semantic slot.
            result['retryCount']=n+1;self.state['slots'][key]=result;save(self.state)
            return
        # A manual "Continue" replaces the latest visible turn. If it completed
        # without changing this semantic position, the old dispatch's message
        # need not be in turnLimit=1. Recover that case just like an empty turn.
        if turn.get('state')=='completed' and self.idle(thread):
            count=record.get('emptyCompletions',0)
            if count>=3:
                self.status('paused','Player completed three turns without an action; operator review needed. No forfeit applied.')
                return
            retry_key=key+':no-action:'+str(count+1)
            self.activate()
            result=self.dispatch(id,retry_key,text+' No accepted action has been recorded at this position yet. Read ./play board, choose your own move, submit it and end your turn.',thread)
            result['emptyCompletions']=count+1;self.state['slots'][key]=result;save(self.state)
    def run(self):
        assert all(p.get('runtimeVerified') for p in self.players.values()),'Verify actual fork, folder and Max settings before play'
        expected=self.setup['protocolSha256']
        assert hashlib.sha256((MATCH/'protocol.json').read_bytes()).hexdigest()==expected
        self.status('active')
        while self.state['status'] in ('active','waiting'):
            saved=json.loads(STATE.read_text())
            if saved.get('status') not in ('active','waiting'):return
            try:
                threads={id:self.snapshot(id) for id in self.players}
                for id,t in threads.items():
                    actual=t.get('modelSelection') or {};expected_model=self.players[id]['modelSelection']
                    def selection(value):
                        return (value.get('instanceId'),value.get('model'),sorted((o['id'],str(o['value'])) for o in value.get('options',[])))
                    if selection(actual)!=selection(expected_model):
                        self.status('paused','Recorded player model or reasoning settings changed; review required.');return
                for path,expected_hash in self.setup.get('integrityFiles',{}).items():
                    file=ROOT/path
                    if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest()!=expected_hash:
                        self.status('paused','Player rules, client or referee integrity changed; review required.');return
                if any(self.stopped(t) for t in threads.values()):
                    self.status('paused','Player thread explicitly interrupted, closed, archived, snoozed or stopped by user.');return
                if hashlib.sha256((MATCH/'protocol.json').read_bytes()).hexdigest()!=expected:
                    self.status('paused','Committed protocol changed; review required.');return
                state=self.ref.state();self.state['game']=state['game'];self.state['score']=state['score'];save(self.state)
                if state['status']=='unfinished':self.status('paused','Unfinished safety-limit game; no score or replacement.');return
                if state['game'] is None:
                    if not all(self.completed(self.state['slots'].get('prepare:'+id),t) for id,t in threads.items()):
                        time.sleep(3);continue
                    self.ref.start_game();continue
                if state.get('result'):
                    i=state['game'];all_done=True
                    for id,t in threads.items():
                        slot=f'reflect:{i}:{id}';record=self.state['slots'].get(slot)
                        if self.completed(record,t):continue
                        all_done=False
                        if self.idle(t):
                            # Reflection requests have no move requirement; only provider errors retry.
                            text=f'Game {i} of the formal 30-game match has ended: {state["result"]}, {state["reason"]}. '
                            text+='Use ./play board and ./play pgn for the finished public game. Reflect using your own reasoning and retained notes; you may update workspace/. Do not access other folders, chess engines, external advice or the opponent’s private material. '
                            text+=('All 30 games are complete. Summarize the actual match result briefly and finish this branch’s bounded goal. Do not start another game.' if i==30 else 'End this reflection turn when ready. The controller will start the next game with colours swapped; do not make a move or poll now.')
                            if not record:self.dispatch(id,slot,text,t)
                            elif (t.get('latestTurn') or {}).get('state') in ('error','failed') or (t.get('session') or {}).get('status')=='error':self.retry(id,slot,text,t)
                    if all_done:
                        if i==30:
                            self.status('complete');logging.info('30-game match complete');return
                        self.ref.start_game();self.status('active')
                    time.sleep(3);continue
                if not all(self.idle(t) for t in threads.values()):time.sleep(3);continue
                id=state['turn'];slot=f'move:{state["game"]}:{state["ply"]}:{id}'
                text=f'Your turn in game {state["game"]}/30 of the formal match. You are '+('White' if state['white']==id else 'Black')+f'; {state["ply"]} plies have been accepted. '
                text+='Read ./play board, choose your own next move with your retained approach, and submit it with ./play move UCI. Use only this folder and the neutral interface under AGENTS.md and MATCH-RULES.md. You may correct an illegal rejection at the same position. After one accepted move (or resignation/draw acceptance), end your turn promptly. Do not poll for the opponent. No external chess help, engine or opponent private notes. Max reasoning is explicitly selected.'
                self.retry(id,slot,text,threads[id])
            except Exception as e:
                # Do not change a chess result on HTTP/host failures.
                logging.warning('Controller infrastructure fault: %s',type(e).__name__)
                self.state['lastInfrastructureError']=type(e).__name__;save(self.state)
                time.sleep(20)
            time.sleep(3)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['prepare','run']);args=parser.parse_args()
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
    lock=(MATCH/'.operator/controller.lock').open('a')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    controller=Controller()
    if args.command=='prepare':controller.prepare()
    else:controller.run()
