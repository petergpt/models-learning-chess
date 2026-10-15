#!/usr/bin/env python3
"""Stop only Fable's session after the user's selected game has a result."""
from pathlib import Path
import datetime as dt
import fcntl
import json
import time
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.operator/fable-pause-after-game.json'
GOAL = ROOT / '.operator/fable-goal.json'
LEDGER = ROOT / 'Chess - Fable-5.1/data/ledger.jsonl'


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def save(path, state):
    state['updatedAt'] = now()
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(state, indent=2) + '\n')
    temporary.replace(path)


def request(path, command=None):
    token = json.loads((ROOT / '.operator/t3-session.json').read_text())['token']
    req = urllib.request.Request('http://127.0.0.1:3773' + path,
        data=json.dumps(command).encode() if command else None,
        headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)


def main():
    while True:
        state = json.loads(STATE.read_text())
        goal = json.loads(GOAL.read_text())
        if state['status'] != 'waiting-for-game':
            return
        if goal.get('status') not in ('pausing', 'paused'):
            state.update(status='cancelled', reason='Pause request superseded.')
            save(STATE, state)
            return
        result = None
        completed = 0
        # Wait for the referee to finish saving its board/dashboard as well as
        # the ledger result before stopping the learner session.
        with (LEDGER.parent / '.lock').open() as lock, LEDGER.open() as ledger:
            fcntl.flock(lock, fcntl.LOCK_SH)
            for line in ledger:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get('kind') == 'result':
                    completed += event.get('score') is not None
                    if event.get('game') == state['game']:
                        result = event
        if result is None:
            time.sleep(2)
            continue
        snapshot = request(f"/api/orchestration/threads/{state['threadId']}?turnLimit=1")['thread']
        if (snapshot.get('session') or {}).get('status') in ('running', 'starting'):
            request('/api/orchestration/dispatch', {
                'type': 'thread.session.stop', 'commandId': str(uuid.uuid4()),
                'threadId': state['threadId'], 'createdAt': now(),
            })
        goal = json.loads(GOAL.read_text())
        goal.update(status='paused', pausedAt=now(), completedGames=completed,
                    reason=f"User-requested pause after game {state['game']} finished.",
                    automaticContinuationEnabled=False)
        save(GOAL, goal)
        state.update(status='paused', pausedAt=now(), resultRecordedAt=result['timestamp'],
                     completedGames=completed)
        save(STATE, state)
        print(f"Fable paused after game {state['game']}; {completed} scored benchmarks retained.", flush=True)
        return


if __name__ == '__main__':
    main()
