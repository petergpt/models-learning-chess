#!/usr/bin/env python3
"""Create a fresh chess-learning run without modifying the released dataset."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import tarfile
import urllib.request

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
ENGINE_SHA256 = '0f83d24cc46d2c66c60f16001af5444873bc112b7d028594513426894c12da19'
ARCHIVE_SHA256 = '9defc0d4e55d49c65a6d042f3e571a39fcea499ade6dbe741b53b8c65e03611f'
ENGINE_URL = 'https://github.com/official-stockfish/Stockfish/releases/download/sf_19/stockfish-linux-x86-64-universal.tar.gz'
ENGINE_REL = 'stockfish/stockfish/stockfish-linux-x86-64-universal'
CHESS_URL = 'https://files.pythonhosted.org/packages/93/09/7d04d7581ae3bb8b598017941781bceb7959dd1b13e3ebf7b6a2cd843bc9/chess-1.11.2.tar.gz'
CHESS_SHA256 = 'a8b43e5678fdb3000695bdaa573117ad683761e5ca38e591c4826eba6d25bb39'


def rules_library():
    """Fetch verified rule-library source separately; pip is not required."""
    path = REPO / '.cache/chess-1.11.2'
    expected = json.loads((HERE / 'rules-hashes.json').read_text())
    if all((path / name).is_file() and sha(path / name) == value for name, value in expected.items()):
        return path
    path.mkdir(parents=True, exist_ok=True)
    archive = path.parent / 'chess-1.11.2.tar.gz.partial'
    print('Downloading the pinned chess-rule library...', flush=True)
    with urllib.request.urlopen(CHESS_URL, timeout=60) as source, archive.open('wb') as target:
        shutil.copyfileobj(source, target)
    if sha(archive) != CHESS_SHA256:
        raise ValueError('Chess-rule source archive checksum failed.')
    with tarfile.open(archive, 'r:gz') as package:
        for member in package:
            parts = Path(member.name).parts
            if not member.isfile() or len(parts) < 2 or '..' in parts:
                continue
            relative = Path(*parts[1:])
            if relative.as_posix() not in expected and relative.as_posix() != 'LICENSE.txt':
                continue
            target = path / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            with package.extractfile(member) as source, target.open('wb') as destination:
                shutil.copyfileobj(source, destination)
    if not all((path / name).is_file() and sha(path / name) == value for name, value in expected.items()):
        raise ValueError('Chess-rule module checksum failed.')
    archive.unlink()
    return path


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def engine_file(supplied=None):
    if supplied:
        path = Path(supplied).resolve()
        if sha(path) != ENGINE_SHA256:
            raise ValueError('The supplied engine does not match the recorded Stockfish 19 binary.')
        return path
    path = REPO / '.cache/stockfish-19/stockfish-linux-x86-64-universal'
    if path.is_file() and sha(path) == ENGINE_SHA256:
        return path
    if platform.system() != 'Linux' or platform.machine().lower() not in ('x86_64', 'amd64'):
        raise ValueError('The pinned opponent requires Linux x86-64. Use a Linux x86-64 environment.')
    path.parent.mkdir(parents=True, exist_ok=True)
    archive = path.parent / 'download.tar.gz.partial'
    print('Downloading the pinned Stockfish 19 release...', flush=True)
    with urllib.request.urlopen(ENGINE_URL, timeout=120) as source, archive.open('wb') as target:
        shutil.copyfileobj(source, target)
    if sha(archive) != ARCHIVE_SHA256:
        raise ValueError('Engine archive checksum failed; the partial download has been retained.')
    temporary = path.with_suffix('.partial')
    with tarfile.open(archive, 'r:gz') as package:
        matches = [m for m in package if m.isfile() and m.name.endswith('/stockfish-linux-x86-64-universal')]
        if len(matches) != 1:
            raise ValueError('Expected exactly one engine executable in the verified archive.')
        with package.extractfile(matches[0]) as source, temporary.open('wb') as target:
            shutil.copyfileobj(source, target)
    if sha(temporary) != ENGINE_SHA256:
        raise ValueError('Engine executable checksum failed.')
    temporary.chmod(0o755)
    temporary.replace(path)
    archive.unlink()
    return path


def create_run(output, model, engine=None, games=200, nodes=1_000_000):
    if games < 1 or nodes < 1:
        raise ValueError('Games and nodes must be positive.')
    output = Path(output).resolve()
    if output.exists() and any(output.iterdir()):
        raise ValueError('Choose a new or empty output directory. Existing runs are never overwritten.')
    template = HERE / 'template'
    opponent = engine_file(engine)
    shutil.copytree(template, output, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc', 'manifest.json'))
    vendor = output / '.arena/vendor/chess-1.11.2'
    if not (vendor / 'chess/__init__.py').is_file():
        shutil.copytree(rules_library(), vendor, dirs_exist_ok=True)
    (output / 'data').mkdir(exist_ok=True)
    (output / 'workspace').mkdir(exist_ok=True)
    target = output / '.arena' / ENGINE_REL
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(opponent, target)
    target.chmod(0o755)
    config_path = output / '.arena/config.json'
    config = json.loads(config_path.read_text())
    config.update(model=model, benchmark_game_limit=games, nodes_per_move=nodes)
    if games != 200 or nodes != 1_000_000:
        config['protocol'] = 'chess-learning-portable-v1-custom-budget'
    config_path.write_text(json.dumps(config, indent=2) + '\n')
    goal = (output / 'GOAL.md').read_text().replace('200 scored', f'{games} scored')
    (output / 'GOAL.md').write_text(goal)
    agents = (output / 'AGENTS.md').read_text().replace('200 scored', f'{games} scored').replace('At 200,', f'At {games},')
    (output / 'AGENTS.md').write_text(agents)
    (output / 'CLAUDE.md').write_text(agents)
    (output / 'play').write_text('''#!/usr/bin/env python3
import os
from pathlib import Path
import shlex
import sys
root = Path(__file__).resolve().parent
runner = shlex.split(os.environ.get('CHESS_JOB_RUNNER', ''))
guard = Path.home() / '.local/bin/t3-job'
if not runner and guard.is_file():
    runner = [str(guard), '--']
command = runner + [sys.executable, '-I', str(root / '.arena/arena.py'), *sys.argv[1:]]
os.execvpe(command[0], command, os.environ)
''')
    (output / 'play').chmod(0o755)
    pinned = [output / name for name in ('play', 'AGENTS.md', 'CLAUDE.md', 'GOAL.md')]
    pinned += [p for p in (output / '.arena').rglob('*')
               if p.is_file() and p.name != 'manifest.json' and '__pycache__' not in p.parts]
    manifest = {p.relative_to(output).as_posix(): sha(p) for p in sorted(pinned)}
    (output / '.arena/manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (output / '.gitignore').write_text('.runner/\n__pycache__/\n')
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True, help='Exact model identifier or label')
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--engine', type=Path, help='Optional existing, checksum-matching Stockfish binary')
    parser.add_argument('--games', type=int, default=200)
    parser.add_argument('--nodes', type=int, default=1_000_000)
    args = parser.parse_args()
    path = create_run(args.output, args.model, args.engine, args.games, args.nodes)
    print(f'Created {path}\nOpen your own agent in this directory. Read AGENTS.md and GOAL.md, then use ./play.')


if __name__ == '__main__':
    main()
