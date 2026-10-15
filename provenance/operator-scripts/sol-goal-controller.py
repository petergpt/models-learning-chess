#!/usr/bin/env python3
"""Continue only the user's bounded GPT-6.1-Sol chess task through normal T3 turns."""
from pathlib import Path
import datetime as dt
import json
import logging
import re
import time
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.operator' / 'sol-goal.json'
CREDENTIAL = ROOT / '.operator' / 't3-session.json'
THREAD = '762f3672-bf9e-4d1d-bbce-e7f7d9f9e3ea'
LEDGER = ROOT / 'Chess - GPT-6.1-Sol' / 'data' / 'ledger.jsonl'
ORIGIN = 'http://127.0.0.1:3773'


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def write_state(state):
    state['updatedAt'] = now()
    temp = STATE.with_suffix('.json.tmp')
    temp.write_text(json.dumps(state, indent=2) + '\n')
    temp.replace(STATE)


def request(path, command=None):
    token = json.loads(CREDENTIAL.read_text())['token']
    req = urllib.request.Request(ORIGIN + path,
        data=json.dumps(command).encode() if command else None,
        headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)


def scored_games():
    count = 0
    if LEDGER.exists():
        with LEDGER.open() as ledger:
            for line in ledger:
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue  # A writer may be appending the final line.
                count += e.get('kind') == 'result' and e.get('score') is not None
    return count


def main():
    state = json.loads(STATE.read_text())
    while state['status'] == 'active':
        # A user/operator may pause the controller by changing its status.
        saved = json.loads(STATE.read_text())
        if saved['status'] != 'active':
            return
        try:
            count = scored_games()
            state['completedGames'] = count
            if count >= 200:
                state['status'] = 'complete'
                state['reason'] = '200 scored benchmark games recorded; no further continuation.'
                write_state(state)
                return
            snapshot = request(f'/api/orchestration/threads/{THREAD}?turnLimit=1')['thread']
            session = snapshot.get('session') or {}
            turn = snapshot.get('latestTurn') or {}
            state['sessionStatus'] = session.get('status')
            if snapshot.get('deletedAt') or snapshot.get('archivedAt') or snapshot.get('snoozedUntil') or snapshot.get('settledOverride'):
                state['status'] = 'paused'
                state['reason'] = 'Thread was explicitly closed, archived, snoozed, or settled.'
                write_state(state)
                return
            if turn.get('state') in ('interrupted', 'error', 'failed') or session.get('status') == 'error':
                state['status'] = 'paused'
                state['reason'] = 'Turn interrupted or failed; no automatic restart.'
                write_state(state)
                return
            foreign_users = [m for m in snapshot.get('messages', []) if m.get('role') == 'user' and m['id'] not in state['ownMessageIds']]
            if any(re.search(r'\b(?:pause|cancel|stop (?:now|this|the run|playing)|do not continue|don.t continue)\b', m.get('text', ''), re.I) for m in foreign_users):
                state['status'] = 'paused'
                state['reason'] = 'User requested a pause or stop.'
                write_state(state)
                return
            pending = any(a.get('kind') in ('approval.requested', 'user-input.requested') for a in snapshot.get('activities', [])[-4:])
            if turn.get('state') == 'completed' and session.get('status') not in ('running', 'starting') and not pending:
                turn_id = turn['turnId']
                if turn_id == state.get('lastContinuedTurn'):
                    write_state(state)
                    time.sleep(20)
                    continue
                message_id = str(uuid.uuid4())
                command = {'type': 'thread.turn.start', 'commandId': str(uuid.uuid4()),
                    'threadId': THREAD, 'message': {'messageId': message_id, 'role': 'user',
                    'text': f'Continue the same authorized independent chess-learning goal in your own folder. {count} of 200 scored benchmarks are recorded. Choose your own next learning or playing steps under AGENTS.md and GOAL.md; keep returning to the fixed benchmarks. Do not inspect any other learner or comparison material. At 200 scored games, stop, summarize honest measured results, and finish. If genuinely blocked, report the concrete fault rather than inventing progress.',
                    'attachments': []}, 'runtimeMode': 'full-access', 'interactionMode': 'default', 'createdAt': now()}
                # Persist the id before dispatch to avoid duplicate continuation on restart.
                state['lastContinuedTurn'] = turn_id
                state['ownMessageIds'].append(message_id)
                write_state(state)
                request('/api/orchestration/dispatch', command)
                state['continuations'] += 1
                logging.info('Continued completed turn; %s/200 benchmarks.', count)
            write_state(state)
        except Exception as error:
            state['status'] = 'paused'
            state['reason'] = 'Controller request failed: ' + type(error).__name__
            write_state(state)
            logging.exception('Controller stopped without restarting the learner.')
            return
        time.sleep(20)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    main()
