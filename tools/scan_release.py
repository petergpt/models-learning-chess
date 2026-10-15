#!/usr/bin/env python3
"""Check the final release for known credentials and credential-shaped strings.

Without --source-root, only generic patterns are used. The optional source root
adds known local credential values to the check; values are never reported.
"""
import argparse
import gzip
import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_release import Cleaner

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED = {'.git', '.cache', '__pycache__', '.venv', 'node_modules'}


def scan_stream(cleaner, source):
    overlap = ''
    while block := source.read(1024 * 1024):
        text = overlap + block.decode('utf-8', errors='ignore')
        cleaner.text(text)
        overlap = text[-8192:]


def scan(root, source_root=None):
    with tempfile.TemporaryDirectory(prefix='chess-release-scan-') as empty:
        cleaner = Cleaner(source_root if source_root else Path(empty))
        files, archive_members, decompressed = 0, 0, 0
        for path in sorted(root.rglob('*')):
            relative = path.relative_to(root)
            if relative.parts[0] == 'runs' or any(part in EXCLUDED for part in relative.parts) or not path.is_file():
                continue
            cleaner.current = relative.as_posix()
            if path.name.endswith('.tar.gz'):
                with tarfile.open(path, 'r|gz') as archive:
                    for member in archive:
                        if not member.isfile():
                            continue
                        with archive.extractfile(member) as source:
                            scan_stream(cleaner, source)
                        archive_members += 1
                        decompressed += member.size
            elif path.suffix == '.gz':
                with gzip.open(path, 'rb') as source:
                    scan_stream(cleaner, source)
            else:
                with path.open('rb') as source:
                    scan_stream(cleaner, source)
            files += 1
        findings = [{'path': name, 'rule': rule, 'occurrences_including_chunk_overlap': count}
                    for (name, rule), count in sorted(cleaner.hits.items())]
        return {'status': 'passed' if not findings else 'review-required', 'files_scanned': files,
                'archive_members_scanned': archive_members, 'archive_member_bytes_scanned': decompressed,
                'known_local_credentials_checked': bool(source_root), 'findings': findings,
                'scope': 'Known credential values and generic API-key/JWT/header/assignment/private-key patterns, including decompressed records and workspace archives. Not a guarantee against every possible secret or private detail.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--source-root', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    report = scan(args.root.resolve(), args.source_root)
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if not report['findings'] else 1)


if __name__ == '__main__':
    main()
