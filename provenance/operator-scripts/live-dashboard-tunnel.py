#!/usr/bin/env python3
"""Start a no-account public tunnel and record the URL issued by Cloudflare."""
from pathlib import Path
import json,re,subprocess,sys

ROOT=Path(__file__).resolve().parent.parent
STATE=ROOT/'.operator/live-dashboard-public.json'

process=subprocess.Popen([str(ROOT/'.operator/cloudflared'),'tunnel','--no-autoupdate','--protocol','http2','--url','http://127.0.0.1:8773'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
try:
 for line in process.stdout:
  match=re.search(r'https://[a-z0-9-]+\.trycloudflare\.com',line)
  if match:
   temporary=STATE.with_suffix('.tmp')
   temporary.write_text(json.dumps({'url':match.group(),'server':'http://127.0.0.1:8773','registrationRequired':False,'temporaryHostname':True},indent=2)+'\n')
   temporary.replace(STATE)
  print(line.rstrip(),flush=True)
 sys.exit(process.wait())
finally:
 if process.poll() is None:process.terminate()
