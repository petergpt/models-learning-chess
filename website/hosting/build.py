"""Build the existing spectator design; live data is stored separately on Cloudflare."""
import importlib.util
import json
import shutil
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('live_dashboard',ROOT.parent/'.operator/live-dashboard-server.py')
dashboard=importlib.util.module_from_spec(spec);spec.loader.exec_module(dashboard)
with urllib.request.urlopen('http://127.0.0.1:8773/data',timeout=20) as response:snapshot=json.load(response)
html=dashboard.page(snapshot).decode()
output=ROOT/'public';output.mkdir(exist_ok=True)
(output/'index.html').write_text(html)
shutil.copytree(ROOT.parent/'surge-site/assets', output/'assets', dirs_exist_ok=True)
(output/'_headers').write_text('/assets/stockfish/19.0.0/*\n  Cache-Control: public, max-age=31536000, immutable\n/assets/spectator-outlook-v1.mjs\n  Cache-Control: public, max-age=0, must-revalidate\n')
print(f'Built {output / "index.html"}')
