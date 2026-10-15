#!/usr/bin/env python3
"""Send public chess snapshots to the hosted feed; never deploy website code."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import logging
import time
import urllib.error
import urllib.request

ROOT=Path(__file__).resolve().parent.parent
CONFIG=ROOT/'.operator/cloudflare-feed-config.json'
STATE=ROOT/'.operator/cloudflare-feed-status.json'
PUBLISH_INTERVAL_SECONDS=5
HEARTBEAT_SECONDS=60

def content_revision(payload):
 """Stable identity for spectator content, independent of refresh timestamps."""
 runs={key:{k:v for k,v in run.items() if k!='generated'} for key,run in payload['runs'].items()}
 public={'runs':runs,'match':payload.get('match')}
 return 'content:'+hashlib.sha256(json.dumps(public,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def now():return dt.datetime.now(dt.timezone.utc).isoformat()

def write_state(value):
 temporary=STATE.with_suffix('.tmp')
 temporary.write_text(json.dumps(value,indent=2)+'\n');temporary.replace(STATE)

def publish(config,payload):
 request=urllib.request.Request(config['url'].rstrip('/')+'/api/ingest',data=json.dumps(payload,separators=(',',':')).encode(),method='PUT',headers={'Authorization':'Bearer '+config['token'],'Content-Type':'application/json','User-Agent':'ChessLearning-Publisher/1.0'})
 with urllib.request.urlopen(request,timeout=20) as response:result=json.load(response)
 if not result.get('ok') or result.get('revision')!=payload['revision']:raise ValueError('Feed acknowledgment mismatch')

def main():
 config=json.loads(CONFIG.read_text())
 if not config.get('url') or not config['url'].startswith('https://'):
  raise ValueError('Hosted feed URL is not configured')
 last_revision=None;last_success=None;last_publish=-float('inf')
 while True:
  started=time.monotonic();retry=PUBLISH_INTERVAL_SECONDS
  try:
   with urllib.request.urlopen('http://127.0.0.1:8773/data',timeout=15) as response:payload=json.load(response)
   payload['revision']=content_revision(payload)
   if payload['revision']!=last_revision or time.monotonic()-last_publish>=HEARTBEAT_SECONDS:
    publish(config,payload);last_revision=payload['revision'];last_success=now();last_publish=time.monotonic()
    write_state({'status':'live','url':config['url'],'lastSuccess':last_success,'snapshotUpdatedAt':payload['updatedAt'],'revision':last_revision})
  except Exception as error:
   code=error.code if isinstance(error,urllib.error.HTTPError) else None
   if code==429:
    try:retry=max(PUBLISH_INTERVAL_SECONDS,min(300,int(error.headers.get('Retry-After','30'))))
    except ValueError:retry=30
   logging.warning('Hosted feed update failed: %s%s',type(error).__name__,f' ({code})' if code else '')
   write_state({'status':'retrying','url':config['url'],'lastSuccess':last_success,'error':type(error).__name__,'httpStatus':code})
  time.sleep(max(1,retry-(time.monotonic()-started)))

if __name__=='__main__':
 logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s');main()
