#!/usr/bin/env python3
"""Create a checksummed, upload-ready ZIP without caches or installed software."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED = {'.git', '.cache', '__pycache__', '.venv', 'node_modules'}


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root, target = args.root.resolve(), args.output.resolve()
    if target.exists() or root in target.parents:
        parser.error('Choose a fresh archive filename outside the release folder.')
    files = [p for p in sorted(root.rglob('*')) if p.is_file() and not p.is_symlink()
             and p.relative_to(root).parts[0] != 'runs'
             and not any(part in EXCLUDED for part in p.relative_to(root).parts)
             and p != root / 'manifest.json']
    manifest = {'format': 'chess-learning-release-v1', 'created_at': dt.datetime.now(dt.timezone.utc).isoformat(),
                'files': {p.relative_to(root).as_posix(): {'sha256': digest(p), 'bytes': p.stat().st_size} for p in files}}
    (root / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    files.append(root / 'manifest.json')
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as archive:
        for path in files:
            compression = zipfile.ZIP_STORED if path.suffix in ('.gz', '.png', '.wasm') else zipfile.ZIP_DEFLATED
            archive.write(path, 'chess-learning/' + path.relative_to(root).as_posix(), compress_type=compression)
    checksum = digest(target)
    target.with_suffix(target.suffix + '.sha256').write_text(checksum + '  ' + target.name + '\n')
    print(json.dumps({'archive': str(target), 'files': len(files), 'bytes': target.stat().st_size,
                      'sha256': checksum}, indent=2))


if __name__ == '__main__':
    main()
