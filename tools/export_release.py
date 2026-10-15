#!/usr/bin/env python3
"""Export this experiment's research data, never installed agent software or accounts.

Run against the original workspace, not against the released data directory.
Known local credentials are read only to replace any occurrences in research
records. Their values are never printed or written to the release.
"""
import argparse
from collections import Counter, defaultdict
import copy
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import sys
import tarfile
import urllib.request

RUNS = {
    'astra': ('Chess - GPT-6-Astra', 'GPT-6 Astra'),
    'opus': ('Chess - Opus-5.5', 'Claude Opus 5.5'),
    'sol': ('Chess - GPT-6.1-Sol', 'GPT-6.1 Sol · 258K'),
    'sol-long-context': ('Chess - GPT-6.1-Sol - Long Context', 'GPT-6.1 Sol · 828K · Medium'),
    'sol-long-context-max': ('Chess - GPT-6.1-Sol - Long Context - Max', 'GPT-6.1 Sol · 828K · Max'),
    'fable': ('Chess - Fable-5.1', 'Claude Fable 5.1'),
}
SITE = 'https://ailearningchess.ai-learning-chess.workers.dev'
SECRET_KEY = re.compile(r'^(?:token|access_?token|refresh_?token|api_?key|ingest_?token|client_?secret|password|authorization|cookie|set-cookie|session_?token|credential)$', re.I)
OPAQUE_KEYS = {'encrypted_content', 'encryptedContent', 'signature', 'resume_cursor_json', 'runtime_payload_json', 'base_instructions'}
PATTERNS = [
    ('api_key', re.compile(r'\b(?:sk-(?:proj-|ant-|svcacct-)?[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b')),
    ('jwt', re.compile(r'\beyJ[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{8,}\b')),
    ('authorization_header', re.compile(r'(?i)\b(?:Bearer|Basic)\s+[A-Za-z0-9._~+/-]{16,}={0,2}')),
    ('private_key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----[\s\S]+?-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
]
ASSIGN = re.compile(r'''(?i)(?<![A-Za-z0-9_])((?:["'](?:access_token|refresh_token|api_key|ingest_token|client_secret|password|authorization|token)["']\s*[:=]|(?:access_token|refresh_token|api_key|ingest_token|client_secret|password|authorization|token)\s*=)\s*["'])([^"'\r\n]{16,})(["'])''')
QUERY = re.compile(r'(?i)([?&](?:token|access_token|api_key|key|secret)=)([A-Za-z0-9._~+/%=-]{16,})')


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')


def jsonl_writer(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    return gzip.open(path, 'wt', encoding='utf-8', compresslevel=6) if path.suffix == '.gz' else path.open('w', encoding='utf-8')


class Cleaner:
    def __init__(self, root):
        self.root = root
        self.current = ''
        self.hits = Counter()
        self.opaque = Counter()
        self.known = set()
        candidates = [root / '.operator/t3-session.json', root / '.operator/cloudflare-feed-config.json',
                      root / '.operator/live-site-publisher-config.json']
        candidates += list((root / 'Matches').rglob('tokens.json'))
        candidates += list((root / 'Matches').rglob('.match-client.json'))
        candidates += list((root / 'cloudflare-site').glob('.dev.vars'))
        for path in candidates:
            if not path.is_file():
                continue
            try:
                value = json.loads(path.read_text())
            except (ValueError, UnicodeError):
                for line in path.read_text(errors='ignore').splitlines():
                    if '=' in line:
                        key, value = line.split('=', 1)
                        if SECRET_KEY.match(key.strip()):
                            self.add_secret(value.strip().strip('"\''))
                continue
            self.collect(value, path.name == 'tokens.json')
        # One compiled alternation avoids repeatedly scanning large provider records.
        self.exact = re.compile('|'.join(re.escape(s) for s in sorted(self.known, key=len, reverse=True))) if self.known else None

    def add_secret(self, value):
        if isinstance(value, str) and len(value) >= 16 and not any(x.isspace() for x in value):
            self.known.add(value)

    def collect(self, obj, force=False):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if force or SECRET_KEY.match(key):
                    self.add_secret(value)
                self.collect(value)
        elif isinstance(obj, list):
            for value in obj:
                self.collect(value)

    def hit(self, rule):
        self.hits[(self.current, rule)] += 1
        return '[REDACTED:' + rule + ']'

    def text(self, value):
        if self.exact:
            value = self.exact.sub(lambda m: self.hit('local_credential'), value)
        for name, pattern in PATTERNS:
            def replace(match, rule=name):
                if rule == 'authorization_header':
                    token = match[0].split()[-1]
                    # Ordinary study notes say things such as "basic reconstruction".
                    # Require token-like character diversity rather than deleting prose.
                    varied = any(c.isdigit() for c in token) or (
                        any(c.isupper() for c in token) and any(c.islower() for c in token))
                    if not varied:
                        return match[0]
                return self.hit(rule)
            value = pattern.sub(replace, value)
        value = ASSIGN.sub(lambda m: m[1] + self.hit('credential_assignment') + m[3]
                           if '[REDACTED:' not in m[2] else m[0], value)
        value = QUERY.sub(lambda m: m[1] + self.hit('credential_query'), value)
        return value

    def obj(self, value, traces=False):
        if isinstance(value, dict):
            result = {}
            for key, item in value.items():
                if traces and key in OPAQUE_KEYS:
                    if item:
                        self.opaque[(self.current, key)] += 1
                    result[key] = None
                elif SECRET_KEY.match(key) and isinstance(item, str) and len(item) >= 16 and '[REDACTED:' not in item:
                    result[key] = self.hit('credential_field')
                else:
                    result[key] = self.obj(item, traces)
            return result
        if isinstance(value, list):
            return [self.obj(x, traces) for x in value]
        if isinstance(value, str):
            # Nested JSON is common in tool outputs; clean fields inside it too.
            stripped = value.lstrip()
            if stripped.startswith(('{', '[')):
                try:
                    decoded = json.loads(value)
                    cleaned = self.obj(decoded, traces)
                    if decoded != cleaned:
                        return canonical(cleaned)
                except (ValueError, RecursionError):
                    pass
            return self.text(value)
        return value

    def bytes(self, content):
        try:
            return self.text(content.decode('utf-8')).encode('utf-8')
        except UnicodeDecodeError:
            if self.exact and self.exact.search(content.decode('latin1')):
                raise ValueError('Credential in binary research artifact: ' + self.current)
            return content


class Export:
    def __init__(self, root, output):
        self.root, self.output = root, output
        self.cleaner = Cleaner(root)
        self.provenance = []
        self.runs, self.games, self.moves, self.snapshot_indexes = [], [], [], []
        self.trace_indexes, self.match = [], None
        vendor = root / RUNS['astra'][0] / '.arena/vendor/chess-1.11.2'
        sys.path.insert(0, str(vendor))
        import chess
        import chess.pgn
        self.chess = chess
        self.chess_pgn = chess.pgn

    def clean_obj(self, value, label, traces=False):
        self.cleaner.current = label
        return self.cleaner.obj(value, traces)

    def copy_file(self, source, dest):
        if source.is_symlink() or not source.is_file():
            return
        label = dest.relative_to(self.output).as_posix()
        self.cleaner.current = label
        data = source.read_bytes()
        if source.suffix == '.gz' and not source.name.endswith('.tar.gz'):
            uncompressed = gzip.decompress(data)
            cleaned = self.cleaner.bytes(uncompressed)
            if cleaned != uncompressed:
                data = gzip.compress(cleaned, mtime=0)
        else:
            data = self.cleaner.bytes(data)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        if source.stat().st_mode & 0o111:
            dest.chmod(0o755)

    def tree(self, source, dest, allowed=None):
        if not source.exists():
            return
        for path in sorted(source.rglob('*')):
            rel = path.relative_to(source)
            if any(part in ('node_modules', '.git', '__pycache__', '.wrangler', '.venv') for part in rel.parts):
                continue
            if not path.is_file() or path.is_symlink() or path.name in ('.dev.vars', 'tokens.json', '.match-client.json'):
                continue
            if allowed and path.suffix not in allowed:
                continue
            self.copy_file(path, dest / rel)

    def snapshots(self, run_id, folder):
        mapping, manifest = {}, []
        for source in sorted((folder / 'data/snapshots').glob('*.tar.gz')):
            label = f'data/runs/{run_id}/snapshots/{source.name}'
            self.cleaner.current = label
            listing, entries, changed = {}, [], False
            with tarfile.open(source, 'r:gz') as archive:
                for member in archive:
                    if not member.isfile() or member.name.startswith('/') or '..' in Path(member.name).parts:
                        raise ValueError('Unsafe workspace archive member in ' + label)
                    with archive.extractfile(member) as handle:
                        raw = handle.read()
                    content = self.cleaner.bytes(raw)
                    changed |= raw != content
                    listing[member.name] = hashlib.sha256(content).hexdigest()
                    entries.append((member, content))
            old_id = source.name.removesuffix('.tar.gz')
            new_id = hashlib.sha256(canonical(listing).encode()).hexdigest()
            if not changed and old_id != new_id:
                raise ValueError('Original snapshot integrity failed: ' + label)
            mapping[old_id] = new_id
            target = self.output / f'data/runs/{run_id}/snapshots/{new_id}.tar.gz'
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                if not changed:
                    shutil.copy2(source, target)
                else:
                    with tarfile.open(target, 'w:gz') as archive:
                        for member, content in entries:
                            member = copy.copy(member)
                            member.size = len(content)
                            archive.addfile(member, io.BytesIO(content))
            manifest.append({'run_id': run_id, 'source_id': old_id, 'snapshot_id': new_id,
                             'members': listing, 'redacted': changed})
        self.snapshot_indexes.extend(manifest)
        return mapping

    def ledger(self, source, target, snapshot_map):
        events, previous, original_previous, changed = [], '0' * 64, '0' * 64, False
        with source.open() as stream, jsonl_writer(target) as dest:
            for number, line in enumerate(stream, 1):
                raw = json.loads(line)
                body = {k: v for k, v in raw.items() if k != 'sha256'}
                if raw['previous'] != original_previous or raw['seq'] != number or hashlib.sha256(canonical(body).encode()).hexdigest() != raw['sha256']:
                    raise ValueError('Original ledger integrity failed: ' + str(source))
                original_previous = raw['sha256']
                event = self.clean_obj(raw, target.relative_to(self.output).as_posix())
                if event.get('snapshot'):
                    event['snapshot'] = snapshot_map[event['snapshot']]
                changed |= event != raw
                if changed:
                    event.pop('sha256', None)
                    event['previous'] = previous
                    event['sha256'] = hashlib.sha256(canonical(event).encode()).hexdigest()
                previous = event['sha256']
                dest.write(canonical(event) + '\n')
                events.append(event)
        self.provenance.append({'path': target.relative_to(self.output).as_posix(),
                                'source_sha256': sha(source), 'source_head': original_previous,
                                'public_head': previous, 'redacted_or_referenced_snapshot_changed': changed,
                                'records': len(events)})
        return events

    def group(self, run_id, mode, events, model):
        grouped = {}
        for e in events:
            if e['kind'] == 'start':
                grouped[e['game']] = {'start': e, 'moves': [], 'illegal': [], 'end': None}
            elif e.get('game') in grouped:
                g = grouped[e['game']]
                if e['kind'] == 'move':
                    g['moves'].append(e)
                elif e['kind'] == 'illegal':
                    g['illegal'].append(e)
                elif e['kind'] == 'result':
                    g['end'] = e
        for number, g in grouped.items():
            start, end = g['start'], g['end']
            board = self.chess.Board(start.get('initial_fen', self.chess.STARTING_FEN))
            game_id = f'{run_id}/{mode}/{number:06d}'
            for event in g['moves']:
                move = self.chess.Move.from_uci(event['uci'])
                if move not in board.legal_moves or board.san(move) != event['san']:
                    raise ValueError('Move replay failed: ' + game_id)
                before = board.fen()
                board.push(move)
                if board.fen() != event['fen']:
                    raise ValueError('Recorded FEN mismatch: ' + game_id)
                self.moves.append({'id': game_id + f'/{event["ply"]:04d}', 'game_id': game_id,
                                   'run_id': run_id, 'mode': mode, 'game_number': number,
                                   'fen_before': before, **event})
            opponent = start['opponent']['id']
            row = {'game_id': game_id, 'run_id': run_id, 'mode': mode, 'game_number': number,
                   'model': model, 'learner_color': start['color'], 'opponent': opponent,
                   'started_at': start['timestamp'], 'ended_at': end['timestamp'] if end else None,
                   'result': end['result'] if end else '*', 'score': end['score'] if end else None,
                   'status': 'scored' if end and end['score'] is not None else 'stopped' if end else 'active',
                   'reason': end['reason'] if end else None, 'plies': len(g['moves']),
                   'illegal_attempts': len(g['illegal']), 'initial_fen': start.get('initial_fen', self.chess.STARTING_FEN),
                   'final_fen': board.fen(), 'start_snapshot': start.get('snapshot'),
                   'end_snapshot': end.get('snapshot') if end else None,
                   'nodes_per_move': start.get('nodes_per_move'), 'opponent_options': start['opponent']['options']}
            self.games.append(row)
            record = self.chess_pgn.Game.from_board(board)
            record.headers.update(Event='Chess Learning', Site=SITE, Round=str(number),
                                  Date=start['timestamp'][:10].replace('-', '.'), Result=row['result'],
                                  White=model if start['color'] == 'white' else 'Stockfish 19',
                                  Black=model if start['color'] == 'black' else 'Stockfish 19',
                                  Mode=mode, RunId=run_id, GameId=game_id,
                                  OpponentSetting=opponent, Termination=row['reason'] or 'in progress')
            destination = self.output / 'data/pgn' / run_id / mode / f'{number:06d}.pgn'
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(str(record) + '\n')

    def export_run(self, run_id, name, label):
        folder = self.root / name
        dest = self.output / 'data/runs' / run_id
        snapshots = self.snapshots(run_id, folder)
        benchmark = self.ledger(folder / 'data/ledger.jsonl', dest / 'ledger.jsonl.gz', snapshots)
        practice = self.ledger(folder / 'data/practice/ledger.jsonl', dest / 'practice/ledger.jsonl.gz', snapshots)
        config = self.clean_obj(json.loads((folder / '.arena/config.json').read_text()), f'provenance/runs/{run_id}/arena/config.json')
        self.group(run_id, 'benchmark', benchmark, config['model'])
        self.group(run_id, 'practice', practice, config['model'])
        self.tree(folder / 'workspace', dest / 'workspace')
        for subfolder in ('games', 'practice/games'):
            self.tree(folder / 'data' / subfolder, dest / 'original-pgn' / subfolder)
        for filename in ('rating-cache.json', 'dashboard.html'):
            self.copy_file(folder / 'data' / filename, dest / 'derived' / filename)
        provenance = self.output / 'provenance/runs' / run_id
        for filename in ('AGENTS.md', 'CLAUDE.md', 'GOAL.md', 'README.md', 'play'):
            self.copy_file(folder / filename, provenance / filename)
        for p in sorted((folder / '.arena').iterdir()):
            if p.is_file() and p.suffix in ('.py', '.html', '.json', '.txt'):
                self.copy_file(p, provenance / 'arena' / p.name)
        self.tree(folder / '.arena/operator-revisions', provenance / 'operator-revisions')
        selected = [g for g in self.games if g['run_id'] == run_id]
        result = {'run_id': run_id, 'label': label, 'model': config['model'],
                  'source_folder': name, 'config': config,
                  'benchmark_started': sum(g['mode'] == 'benchmark' for g in selected),
                  'benchmark_scored': sum(g['mode'] == 'benchmark' and g['status'] == 'scored' for g in selected),
                  'benchmark_active': sum(g['mode'] == 'benchmark' and g['status'] == 'active' for g in selected),
                  'practice_sessions': sum(g['mode'] == 'practice' for g in selected),
                  'workspace_snapshots': len(snapshots),
                  'benchmark_events': len(benchmark), 'practice_events': len(practice)}
        self.runs.append(result)
        print('Exported run:', run_id, result['benchmark_scored'], 'scored benchmarks', flush=True)

    def traces(self, run_id, source, parent=None):
        path = Path(source)
        dest = self.output / 'data/traces' / run_id / 'events.jsonl.gz'
        kinds, records = Counter(), 0
        with path.open() as stream, jsonl_writer(dest) as output:
            for sequence, line in enumerate(stream, 1):
                original = json.loads(line)
                record = self.clean_obj(original, f'data/traces/{run_id}/events.jsonl.gz', traces=True)
                # Account-local path names are not part of the experimental protocol.
                for key in ('cwd', 'projectPath', 'transcriptPath', 'sessionPath'):
                    record.pop(key, None)
                payload = record.get('payload')
                if record.get('type') == 'session_meta' and isinstance(payload, dict):
                    payload = {k: v for k, v in payload.items() if k in (
                        'timestamp', 'cli_version', 'originator', 'source', 'model_provider', 'forked_from_id')}
                    record['payload'] = payload
                entry = {'run_id': run_id, 'source_sequence': sequence,
                         'timestamp': record.get('timestamp'), 'kind': record.get('type', 'unknown'),
                         'record': record}
                output.write(canonical(entry) + '\n')
                kinds[entry['kind']] += 1
                records += 1
        self.trace_indexes.append({'run_id': run_id, 'path': dest.relative_to(self.output).as_posix(),
                                   'source_sha256': sha(path), 'source_bytes': path.stat().st_size,
                                   'public_bytes_gzip': dest.stat().st_size, 'records': records,
                                   'record_types': dict(kinds), 'inherits_from': parent,
                                   'format': 'normalized native event export; credentials and opaque runtime fields removed'})
        print('Exported trace:', run_id, records, 'records', flush=True)

    def export_match(self):
        folder = self.root / 'Matches/Astra vs Opus - 30 games'
        db = sqlite3.connect((folder / '.referee/match.sqlite').as_uri() + '?mode=ro', uri=True)
        db.row_factory = sqlite3.Row
        db.execute('BEGIN')
        games = [dict(g) for g in db.execute('SELECT * FROM games ORDER BY id')]
        raw_events = [dict(e) for e in db.execute('SELECT * FROM events ORDER BY seq')]
        db.close()
        dest = self.output / 'data/match'
        events = []
        previous = source_previous = '0' * 64
        changed = False
        for raw in raw_events:
            raw['payload'] = json.loads(raw['payload'])
            source_body = {k: raw[k] for k in ('at', 'kind', 'game', 'actor', 'payload', 'previous')}
            if raw['previous'] != source_previous or hashlib.sha256(json.dumps(source_body, sort_keys=True, separators=(',', ':')).encode()).hexdigest() != raw['hash']:
                raise ValueError('Match source chain failed.')
            source_previous = raw['hash']
            event = self.clean_obj(raw, 'data/match/events.jsonl.gz')
            changed |= raw != event
            if changed:
                event['previous'] = previous
                body = {k: event[k] for k in ('at', 'kind', 'game', 'actor', 'payload', 'previous')}
                event['hash'] = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
            previous = event['hash']
            events.append(event)
        with jsonl_writer(dest / 'events.jsonl.gz') as output:
            for event in events:
                output.write(canonical(event) + '\n')
        write_json(dest / 'protocol.json', self.clean_obj(json.loads((folder / 'protocol.json').read_text()), 'data/match/protocol.json'))
        self.copy_file(folder / 'MATCH-RULES.md', dest / 'MATCH-RULES.md')
        labels = {'astra': 'GPT-6 Astra', 'opus': 'Claude Opus 5.5'}
        for raw in games:
            game_id = f'astra-opus/match/{raw["id"]:06d}'
            board = self.chess.Board()
            for ply, event in enumerate(json.loads(raw['moves']), 1):
                event = self.clean_obj(event, 'data/moves.jsonl.gz')
                before = board.fen()
                move = self.chess.Move.from_uci(event['uci'])
                if move not in board.legal_moves or board.san(move) != event['san']:
                    raise ValueError('Match move replay failed.')
                board.push(move)
                if event.get('fen') and event['fen'] != board.fen():
                    raise ValueError('Match FEN mismatch.')
                self.moves.append({'id': game_id + f'/{ply:04d}', 'game_id': game_id,
                                   'run_id': 'astra-opus', 'mode': 'match', 'game_number': raw['id'],
                                   'fen_before': before, 'fen': board.fen(), 'ply': ply, **event})
            row = {'game_id': game_id, 'run_id': 'astra-opus', 'mode': 'match', 'game_number': raw['id'],
                   'model': None, 'learner_color': None, 'opponent': None,
                   'white': labels[raw['white']], 'black': labels[raw['black']],
                   'started_at': raw['started'], 'ended_at': raw['ended'], 'result': raw['result'] or '*',
                   'score': None, 'status': 'scored' if raw['result'] and raw['result'] != '*' else 'active',
                   'reason': raw['reason'], 'plies': board.ply(),
                   'illegal_attempts': sum(e['kind'] == 'illegal_submission' and e['game'] == raw['id'] for e in events),
                   'initial_fen': self.chess.STARTING_FEN, 'final_fen': board.fen()}
            self.games.append(row)
            record = self.chess_pgn.Game.from_board(board)
            record.headers.update(Event='Astra vs Opus — 30 games', Site=SITE, Round=str(raw['id']),
                                  Date=raw['started'][:10].replace('-', '.'), Result=row['result'],
                                  White=row['white'], Black=row['black'], Mode='match',
                                  RunId='astra-opus', GameId=game_id, Termination=raw['reason'] or 'in progress')
            path = self.output / 'data/pgn/astra-opus/match' / f'{raw["id"]:06d}.pgn'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(str(record) + '\n')
        for name, run_id in (('GPT-6 Astra', 'astra'), ('Claude Opus 5.5', 'opus')):
            player = folder / name
            self.tree(player / 'workspace', dest / 'players' / run_id / 'workspace')
            for file in ('AGENTS.md', 'CLAUDE.md', 'GOAL.md', 'MATCH-RULES.md'):
                self.copy_file(player / file, dest / 'players' / run_id / file)
        # Checkpoints contain only the original learner workspace/instructions/ledger.
        for source in (folder / '.operator/checkpoints').glob('*.tar.gz'):
            self.cleaner.current = 'data/match/checkpoints/' + source.name
            with tarfile.open(source, 'r:gz') as archive:
                members = [(copy.copy(m), self.cleaner.bytes(archive.extractfile(m).read()))
                           for m in archive if m.isfile() and not m.name.startswith('/') and '..' not in Path(m.name).parts]
            target = dest / 'checkpoints' / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            with tarfile.open(target, 'w:gz') as archive:
                for member, content in members:
                    member.size = len(content)
                    archive.addfile(member, io.BytesIO(content))
        setup = json.loads((folder / '.operator/setup.json').read_text())
        for player, entry in setup['players'].items():
            self.traces('match-' + player, entry['forkNativePath'], parent=player)
        self.copy_file(folder / '.operator/controller.json', dest / 'controller-events.json')
        self.provenance.append({'path': 'data/match/events.jsonl.gz', 'source_head': source_previous,
                                'public_head': previous, 'redacted': changed, 'records': len(events)})
        self.match = {'run_id': 'astra-opus', 'games': len(games), 'scored': sum(g['result'] != '*' and g['result'] is not None for g in games),
                      'events': len(events), 'plies': sum(len(json.loads(g['moves'])) for g in games)}

    def source_structure(self):
        source = self.root / RUNS['astra'][0]
        template = self.output / 'harness/template'
        for name in ('arena.py', 'practice.py', 'rating.py', 'viewer.html', 'config.json', 'dependencies.json', 'test_arena.py', 'test_practice.py', 'test_rating.py'):
            self.copy_file(source / '.arena' / name, template / '.arena' / name)
        # No agent implementation, executable, account directory, or native resume file is copied.
        independent = self.root / RUNS['sol'][0]
        agents = (independent / 'AGENTS.md').read_text()
        agents = agents.replace("- Follow the user's shared memory protections. `./play` already runs through `t3-job`. Use that wrapper for other memory-intensive work too. No limit is imposed on learning tokens; host/storage/provider limits still apply.",
                                '- Follow the execution host resource limits. The play launcher uses CHESS_JOB_RUNNER when configured and detects a local t3-job installation. No learning-token cap is imposed.')
        for name in ('AGENTS.md', 'CLAUDE.md'):
            (template / name).write_text(agents)
        goal = (independent / 'GOAL.md').read_text()
        goal = re.sub(r'This is a fresh, independent[^\n]+', 'This is a fresh independent run with an empty workspace. Complete 200 scored benchmark games, then stop and report what the measurements show.', goal)
        (template / 'GOAL.md').write_text(goal)
        self.copy_file(self.root / '.operator/model-effort-audit.json', self.output / 'provenance/model-effort-audit.json')
        vendor = source / '.arena/vendor/chess-1.11.2'
        write_json(self.output / 'harness/rules-hashes.json', {
            p.relative_to(vendor).as_posix(): sha(p) for p in sorted((vendor / 'chess').glob('*.py'))})
        for path in (self.root / '.operator').glob('*initial-instructions.txt'):
            self.copy_file(path, self.output / 'provenance/initial-prompts' / path.name)
        for path in (self.root / '.operator').glob('*.py'):
            if 'release' not in path.name and 'open-source' not in path.name and path.name not in ('t3-session-renew.py',):
                self.copy_file(path, self.output / 'provenance/operator-scripts' / path.name)
        for folder in ('learning-assessment', 'claude-review', 'audits'):
            self.tree(self.root / '.operator' / folder, self.output / 'analysis' / folder,
                      {'.py', '.md', '.json', '.jsonl', '.csv', '.html', '.png'})
        for path in (self.root / 'deliverables').glob('*.md'):
            if 'open-source' not in path.name:
                self.copy_file(path, self.output / 'analysis/reports' / path.name)

    def website(self):
        website = self.output / 'website'
        website.mkdir(exist_ok=True)
        headers = {'User-Agent': 'Chess-Learning-Research-Archive/1.0'}
        downloaded = []
        for url_path, filename in (('/', 'index.html'), ('/data', 'data')):
            request = urllib.request.Request(SITE + url_path, headers=headers)
            with urllib.request.urlopen(request, timeout=45) as response:
                data = response.read()
            self.cleaner.current = 'website/' + filename
            (website / filename).write_bytes(self.cleaner.bytes(data))
            downloaded.append({'url': SITE + url_path, 'path': 'website/' + filename})
        self.tree(self.root / 'surge-site/assets', website / 'assets')
        # Custom hosting source only; no node_modules, provider runtime, or .dev.vars.
        for name in ('worker.js', 'build.py', 'wrangler.jsonc', 'package.json', 'package-lock.json'):
            self.copy_file(self.root / 'cloudflare-site' / name, website / 'hosting' / name)
        write_json(website / 'capture.json', {'captured_at': dt.datetime.now(dt.timezone.utc).isoformat(),
                                             'deployed_url': SITE, 'files': downloaded,
                                             'screenshots': ['docs/screenshots/overview.png', 'docs/screenshots/tournament.png']})

    def finish(self):
        self.games.sort(key=lambda g: (g['run_id'], g['mode'], g['game_number']))
        self.moves.sort(key=lambda g: (g['run_id'], g['mode'], g['game_number'], g['ply']))
        for filename, rows in (('games.jsonl', self.games), ('moves.jsonl.gz', self.moves), ('snapshots.jsonl.gz', self.snapshot_indexes)):
            with jsonl_writer(self.output / 'data' / filename) as output:
                for row in rows:
                    output.write(canonical(row) + '\n')
        fields = ['game_id', 'run_id', 'mode', 'game_number', 'model', 'learner_color', 'white', 'black', 'opponent', 'started_at', 'ended_at', 'result', 'score', 'status', 'reason', 'plies', 'illegal_attempts']
        with (self.output / 'data/games.csv').open('w', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=fields, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(self.games)
        with gzip.open(self.output / 'data/all-games.pgn.gz', 'wt', encoding='utf-8') as output:
            for path in sorted((self.output / 'data/pgn').rglob('*.pgn')):
                output.write(path.read_text() + '\n')
        totals = {'learning_runs': len(self.runs), 'benchmark_scored': sum(r['benchmark_scored'] for r in self.runs),
                  'benchmark_active': sum(r['benchmark_active'] for r in self.runs),
                  'practice_sessions': sum(r['practice_sessions'] for r in self.runs),
                  'match_games': self.match['scored'], 'game_session_starts': len(self.games),
                  'accepted_plies': len(self.moves), 'workspace_snapshots': len(self.snapshot_indexes),
                  'trace_files': len(self.trace_indexes), 'trace_records': sum(t['records'] for t in self.trace_indexes)}
        write_json(self.output / 'data/index.json', {'schema_version': '1.0', 'snapshot_date': '2026-10-15',
                   'deployed_url': SITE, 'totals': totals, 'runs': self.runs, 'match': self.match,
                   'notes': ['Benchmark, practice, and match modes are separate.', 'Run names are labels; native turn metadata records settings changes.',
                             'The two match traces inherit history from original learner sessions; do not count inherited events as new activity.']})
        write_json(self.output / 'data/traces/index.json', self.trace_indexes)
        write_json(self.output / 'provenance/ledger-provenance.json', self.provenance)
        report = {'policy': 'Retain research text, including provider-returned thinking and summaries. Remove credentials and opaque runtime/resume fields. Do not bundle installed agent software, account directories, or authentication files.',
                  'secret_substitutions': [{'path': path, 'rule': rule, 'count': count} for (path, rule), count in sorted(self.cleaner.hits.items())],
                  'opaque_fields_removed': [{'path': path, 'field': field, 'count': count} for (path, field), count in sorted(self.cleaner.opaque.items())],
                  'excluded_source_categories': ['Installed Claude Code and Codex software', 'Account/authentication/configuration directories',
                     'Native session-resume files and encrypted/signature fields', 'Installed agent/deployment dependency directories, native engine executables, caches and lock files; the upstream browser-engine source archive is retained intact',
                     'Redundant intermediate SDK fork copy', 'Unrelated conversations and whole-application databases'],
                  'original_experiment_files_modified': False}
        write_json(self.output / 'provenance/redactions.json', report)
        print(json.dumps({'totals': totals, 'secret_substitutions': sum(self.cleaner.hits.values()),
                          'opaque_fields_removed': sum(self.cleaner.opaque.values()), 'output': str(self.output)}, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--replace-generated', action='store_true', help='Replace only data/provenance/analysis/website from an earlier export')
    args = parser.parse_args()
    root, output = args.source_root.resolve(), args.output.resolve()
    if root == output or root in output.parents and output.name.startswith('Chess - '):
        parser.error('Output must be a separate release directory.')
    output.mkdir(parents=True, exist_ok=True)
    generated = ('data', 'provenance', 'analysis', 'website')
    if any((output / name).exists() for name in generated):
        if not args.replace_generated:
            parser.error('Generated content already exists; use a new output or --replace-generated.')
        for name in generated:
            if (output / name).is_dir():
                shutil.rmtree(output / name)
    exporter = Export(root, output)
    for run_id, (name, label) in RUNS.items():
        exporter.export_run(run_id, name, label)
    sources = json.loads((root / '.operator/model-effort-audit.json').read_text())['runs']
    for run_id in RUNS:
        exporter.traces(run_id, sources[run_id]['source'])
    exporter.export_match()
    exporter.source_structure()
    exporter.website()
    exporter.finish()


if __name__ == '__main__':
    main()
