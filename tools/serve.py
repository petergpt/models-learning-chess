#!/usr/bin/env python3
"""View the frozen dashboard locally: python3 tools/serve.py --port 8000."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    website = Path(__file__).resolve().parent.parent / 'website'
    handler = partial(SimpleHTTPRequestHandler, directory=str(website))
    server = ThreadingHTTPServer(('127.0.0.1', args.port), handler)
    print(f'Frozen dashboard: http://127.0.0.1:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
