#!/usr/bin/env python3
"""Make one authorized attempt to restore the old URL as a static redirect."""
from pathlib import Path
import datetime as dt
import json
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.operator/surge-redirect-status.json'
DOMAIN = 'ai-learning-to-play-chess.surge.sh'


def save(value):
    value['updatedAt'] = dt.datetime.now(dt.timezone.utc).isoformat()
    temporary = STATE.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(STATE)


def main():
    state = json.loads(STATE.read_text())
    state['status'] = 'publishing'
    state['lastAttemptAt'] = dt.datetime.now(dt.timezone.utc).isoformat()
    save(state)
    command = [str(ROOT / '.operator/surge-cli/node_modules/.bin/surge'),
               str(ROOT / 'surge-redirect'), DOMAIN]
    try:
        result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                text=True, timeout=120, stdin=subprocess.DEVNULL)
        output = result.stdout + result.stderr
        if result.returncode != 0 or 'Success!' not in output:
            state['status'] = 'blocked' if 'Rate limited' in output else 'failed'
            state['reason'] = ('Surge domain rate limit still active; no further retries scheduled.'
                               if 'Rate limited' in output else 'Surge rejected redirect publishing.')
            state['exitCode'] = result.returncode
        else:
            state['status'] = 'published'
            state.pop('reason', None)
            state['publishedAt'] = dt.datetime.now(dt.timezone.utc).isoformat()
            request = urllib.request.Request('https://' + DOMAIN + '/',
                headers={'User-Agent': 'ChessLearning-Verifier/1.0'})
            try:
                with urllib.request.urlopen(request, timeout=20) as response:
                    body = response.read().decode()
                    state['verified'] = (response.status == 200 and
                        'location.replace(destination.href)' in body and
                        state['destination'] in body)
            except (OSError, ValueError):
                state['verified'] = False
    except (OSError, subprocess.TimeoutExpired) as error:
        state['status'] = 'failed'
        state['reason'] = type(error).__name__
    save(state)
    print(json.dumps({key: state.get(key) for key in ['status', 'url', 'verified', 'reason']}))


if __name__ == '__main__':
    main()
