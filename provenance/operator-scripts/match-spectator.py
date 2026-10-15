"""Public tournament activity: session metadata and explicitly public referee events.

Never reads native transcripts, private notes, reasoning, or tool output.
"""
from pathlib import Path
import datetime as dt
import json
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
PLAYERS = ('astra', 'opus')

def native_status(thread_id):
    token = json.loads((ROOT / '.operator/t3-session.json').read_text())['token']
    req = urllib.request.Request('http://127.0.0.1:3773/api/orchestration/threads/' + thread_id + '?turnLimit=1',
                                 headers={'Authorization': 'Bearer ' + token})
    with urllib.request.urlopen(req, timeout=2) as response:
        thread = json.load(response)['thread']
    turn = thread.get('latestTurn') or {}
    return {'state': turn.get('state'), 'startedAt': turn.get('startedAt'),
            'completedAt': turn.get('completedAt'),
            'session': (thread.get('session') or {}).get('status')}

def after(value, reference):
    try:
        return dt.datetime.fromisoformat(value.replace('Z', '+00:00')) >= dt.datetime.fromisoformat(reference.replace('Z', '+00:00')) - dt.timedelta(seconds=1)
    except (ValueError, AttributeError):
        return False

def player_activity(public, controller, sessions):
    result = {}
    for player in PLAYERS:
        native = sessions.get(player) or {}
        busy = native.get('state') in ('running', 'starting', 'pending') or native.get('session') in ('running', 'starting')
        prefix = ('reflect:' + str(public['currentGame']) + ':' + player) if public['turn'] is None else ('move:' + str(public['currentGame']) + ':' + str(public['games'][-1]['ply']) + ':' + player)
        record = controller.get('slots', {}).get(prefix) or {}
        requested = (record.get('command') or {}).get('createdAt')
        own_request = bool(requested and after(native.get('startedAt'), requested))
        phase, since = 'waiting', None
        if public['status'] in ('paused', 'unfinished') or controller.get('status') == 'paused':
            phase = 'paused'
        elif public['status'] == 'waiting' and public['turn'] == player:
            phase = 'retrying'
        elif public['turn'] is None:
            phase = 'reflecting' if busy and own_request else ('complete' if public['status'] == 'complete' else 'ready')
            since = native.get('startedAt') if phase == 'reflecting' else None
        elif public['turn'] == player:
            phase = 'thinking' if busy and own_request else ('connecting' if not native else 'queued')
            since = native.get('startedAt') if phase == 'thinking' else None
        elif busy:
            phase = 'submitted'
        result[player] = {'phase': phase, 'since': since}
    return result

def public_timeline(referee, public):
    if public['currentGame'] is None:
        return []
    with referee.connect() as db:
        db.execute('BEGIN')
        rows = db.execute("SELECT seq,at,game,actor,payload FROM events WHERE kind='move' AND game=? AND seq<=? ORDER BY seq DESC LIMIT 24",
                          (public['currentGame'], public['eventSequence'])).fetchall()
    items = []
    for row in reversed(rows):
        payload = json.loads(row['payload'])
        item = {'seq': row['seq'], 'game': row['game'], 'player': row['actor'],
                'ply': payload['ply'], 'san': payload['san'], 'at': row['at']}
        # This field was explicitly submitted as a brief public move comment.
        comment = payload.get('note', '').strip()[:240]
        if comment:
            item['comment'] = comment
        items.append(item)
    return items

def enrich(referee, public):
    setup_path = referee.folder / '.operator/setup.json'
    controller_path = referee.folder / '.operator/controller.json'
    if not setup_path.exists() or not controller_path.exists():
        return public
    setup = json.loads(setup_path.read_text())
    controller = json.loads(controller_path.read_text())
    sessions = {}
    for player in PLAYERS:
        try:
            sessions[player] = native_status(setup['players'][player]['threadId'])
        except (OSError, ValueError, KeyError):
            sessions[player] = None
    return {**public, 'activity': player_activity(public, controller, sessions),
            'timeline': public_timeline(referee, public)}
