#!/usr/bin/env python3
"""Record elapsed decision time while forwarding own commands to ./play.

No chess imports, move generation, board inspection, evaluation, or selection.
The caller supplies every command and move. ./play remains the sole referee
and opponent interface. Elapsed time includes communication/tool delays.
"""
import datetime
import json
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent.parent
STATE = BASE / 'workspace/trials/decision-clock-09-state.json'
LOG = BASE / 'workspace/trials/decision-clock-09.jsonl'
TARGET = 20.0

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

args = sys.argv[1:]
if not args or args == ['--help']:
    print('Usage: python3 workspace/decision-clock.py [practice] start|move|board|end|resign ...')
    raise SystemExit(0)
mode = 'practice' if args[0] == 'practice' else 'benchmark'
action_index = 1 if mode == 'practice' else 0
if len(args) <= action_index:
    raise SystemExit('Missing referee action')
action = args[action_index]
state = json.loads(STATE.read_text()) if STATE.exists() else {}
submitted_monotonic = time.monotonic()
submitted_at = utc()
elapsed = None
if action == 'move' and state.get('active') and state.get('mode') == mode:
    elapsed = submitted_monotonic - state['available_monotonic']
    print(f'[decision-clock] {elapsed:.2f}s elapsed; target {TARGET:.0f}s; includes tool/communication delays', flush=True)
result = subprocess.run([str(BASE / 'play'), *args], cwd=BASE, text=True, capture_output=True)
returned_monotonic = time.monotonic()
returned_at = utc()
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
failed = result.returncode != 0 or '"error"' in result.stdout
if action == 'start' and not failed:
    state = {'active': True, 'mode': mode, 'session': returned_at,
             'available_monotonic': returned_monotonic, 'available_at': returned_at}
elif action == 'move' and not failed:
    state.update(active=True, mode=mode, available_monotonic=returned_monotonic,
                 available_at=returned_at)
elif action in ('end', 'resign') and not failed:
    state['active'] = False
record = {'mode': mode, 'action': action, 'session': state.get('session'),
          'command': args, 'submitted_at': submitted_at, 'returned_at': returned_at,
          'elapsed_seconds': round(elapsed, 3) if elapsed is not None else None,
          'target_seconds': TARGET, 'over_target': elapsed > TARGET if elapsed is not None else None,
          'referee_returncode': result.returncode, 'referee_error': failed}
with LOG.open('a') as f:
    f.write(json.dumps(record) + '\n')
STATE.write_text(json.dumps(state, indent=2) + '\n')
raise SystemExit(result.returncode)
