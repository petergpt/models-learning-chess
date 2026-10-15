"""Fetch pinned browser-only engine assets and their corresponding GPL source."""
from pathlib import Path
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / 'surge-site/assets/stockfish/19.0.0'
COMMIT = '54fde71d90c7c403964f6cacef48f7bbec495df1'
BASE = 'https://unpkg.com/stockfish@19.0.0/bin/'
FILES = {
    'stockfish-19-lite-single.js': BASE + 'stockfish-19-lite-single.js',
    'stockfish-19-lite-single.wasm': BASE + 'stockfish-19-lite-single.wasm',
    'Copying.txt': f'https://raw.githubusercontent.com/nmrugg/stockfish.js/{COMMIT}/Copying.txt',
    'AUTHORS': f'https://raw.githubusercontent.com/nmrugg/stockfish.js/{COMMIT}/AUTHORS',
    'stockfish-source.tar.gz': f'https://codeload.github.com/nmrugg/stockfish.js/tar.gz/{COMMIT}',
}

def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    manifest = {'package': 'stockfish', 'version': '19.0.0', 'flavour': 'lite-single',
                'sourceCommit': COMMIT, 'license': 'GPL-3.0', 'files': {}}
    for name, url in FILES.items():
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read(8_000_001)
        if len(data) > 8_000_000:
            raise ValueError('Unexpected asset size')
        if name.endswith('.wasm') and not data.startswith(b'\x00asm'):
            raise ValueError('Invalid WASM asset')
        (OUTPUT / name).write_bytes(data)
        manifest['files'][name] = {'url': url, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
        print(name, len(data), 'bytes')
    (OUTPUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

if __name__ == '__main__':
    main()
