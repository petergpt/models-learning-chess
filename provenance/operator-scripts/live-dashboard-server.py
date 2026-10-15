#!/usr/bin/env python3
"""Public read-only spectator server. No file browsing, writes, or learner control."""
from pathlib import Path
import argparse,gzip,importlib.util,json,logging,threading,time
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parent.parent
STATE=ROOT/'.operator/live-dashboard-status.json'
ENGINE_ASSETS='/assets/stockfish/19.0.0/'
ASSETS={'/assets/spectator-outlook-v1.mjs':('text/javascript; charset=utf-8',False)}
ASSETS.update({ENGINE_ASSETS+name:(content_type,True) for name,content_type in {
 'stockfish-19-lite-single.js':'text/javascript; charset=utf-8',
 'stockfish-19-lite-single.wasm':'application/wasm',
 'Copying.txt':'text/plain; charset=utf-8',
 'AUTHORS':'text/plain; charset=utf-8',
 'stockfish-source.tar.gz':'application/gzip',
 'manifest.json':'application/json; charset=utf-8',
}.items()})

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path)
 result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result

source=module('spectator_source',ROOT/'.operator/live-site-publisher.py')
compact=module('spectator_compact',ROOT/'surge-site/build.py').compact

class SnapshotCache:
 def __init__(self):self.lock=threading.Lock();self.value=None;self.json=None;self.gzip=None;self.states={};self.next_states=0
 def update(self):
  if time.monotonic()>=self.next_states:self.states=source.thread_states();self.next_states=time.monotonic()+20
  value=compact(source.snapshot(self.states));encoded=json.dumps(value,separators=(',',':')).encode()
  compressed=gzip.compress(encoded)
  with self.lock:self.value=value;self.json=encoded;self.gzip=compressed
  state={'status':'live','updatedAt':value['updatedAt'],'revision':value['revision'],'models':{key:{'games':sum(bool(g.get('end')) and g['end'].get('score') is not None for g in r['games']),'state':r['liveState']} for key,r in value['runs'].items()}}
  temporary=STATE.with_suffix('.tmp');temporary.write_text(json.dumps(state,indent=2)+'\n');temporary.replace(STATE)
 def run(self):
  while True:
   started=time.monotonic()
   try:self.update()
   except Exception as error:logging.warning('Live data refresh failed: %s',type(error).__name__)
   time.sleep(max(1,5-(time.monotonic()-started)))
 def get(self):
  with self.lock:return self.value,self.json,self.gzip

def page(snapshot):
 template=(ROOT/'surge-site/template.html').read_text()
 template=template.replace('let liveRevision=null,pendingSnapshot=null,currentView=',
  'let liveRevision='+json.dumps(snapshot['revision'])+',pendingSnapshot=null,currentView=')
 template=template.replace('snapshotUpdatedAt=null;', 'snapshotUpdatedAt='+json.dumps(snapshot['updatedAt'])+';')
 template=template.replace('__MATCH_DATA__',json.dumps(snapshot.get('match'),separators=(',',':')).replace('<','\\u003c'))
 return template.replace('__DATA__',json.dumps(snapshot['runs'],separators=(',',':')).replace('<','\\u003c')).encode()

class Handler(BaseHTTPRequestHandler):
 protocol_version='HTTP/1.1'
 def log_message(self,*args):pass
 def send(self,status,body=b'',content_type='application/json; charset=utf-8',extra=None):
  self.send_response(status)
  for key,value in {'Content-Type':content_type,'Content-Length':str(len(body)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Access-Control-Allow-Origin':'*',**(extra or {})}.items():self.send_header(key,value)
  self.end_headers()
  if self.command!='HEAD' and body:
   try:self.wfile.write(body)
   except (BrokenPipeError,ConnectionResetError):pass
 def do_HEAD(self):self.do_GET()
 def do_GET(self):
  path=urlsplit(self.path).path
  if path in ASSETS:
   content_type,immutable=ASSETS[path]
   asset=ROOT/'surge-site'/path.lstrip('/')
   if not asset.is_file():self.send(404,b'{"error":"Not found"}');return
   cache_control='public, max-age=31536000, immutable' if immutable else 'public, max-age=0, must-revalidate'
   self.send(200,asset.read_bytes(),content_type,{'Cache-Control':cache_control});return
  if path not in ['/', '/index.html','/data','/data.json','/health']:
   self.send(404,b'{"error":"Not found"}');return
  snapshot,encoded,compressed=self.server.cache.get()
  if not snapshot:self.send(503,b'{"error":"Live data is starting"}');return
  etag='W/"'+snapshot['revision']+'"'
  if path in ['/data','/data.json']:
   validators=[tag.strip().removeprefix('W/') for tag in self.headers.get('If-None-Match','').split(',')]
   if '*' in validators or etag.removeprefix('W/') in validators:self.send(304,extra={'ETag':etag});return
   if 'gzip' in self.headers.get('Accept-Encoding',''):self.send(200,compressed,extra={'ETag':etag,'Content-Encoding':'gzip','Vary':'Accept-Encoding'})
   else:self.send(200,encoded,extra={'ETag':etag,'Vary':'Accept-Encoding'})
  elif path=='/health':self.send(200,json.dumps({'updatedAt':snapshot['updatedAt'],'revision':snapshot['revision']}).encode())
  else:
   body=page(snapshot);headers={'Vary':'Accept-Encoding'}
   if 'gzip' in self.headers.get('Accept-Encoding',''):body=gzip.compress(body);headers['Content-Encoding']='gzip'
   self.send(200,body,'text/html; charset=utf-8',headers)
 def do_OPTIONS(self):
  if urlsplit(self.path).path not in ['/data','/data.json','/health']:self.send(404);return
  self.send(204,extra={'Access-Control-Allow-Methods':'GET, HEAD, OPTIONS','Access-Control-Allow-Headers':'If-None-Match'})
 def do_POST(self):self.send(405,b'{"error":"Read only"}',extra={'Allow':'GET, HEAD, OPTIONS'})
 do_PUT=do_POST;do_PATCH=do_POST;do_DELETE=do_POST

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8773);args=parser.parse_args()
 cache=SnapshotCache();cache.update()
 server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler);server.daemon_threads=True;server.cache=cache
 threading.Thread(target=cache.run,daemon=True).start()
 logging.info('Read-only chess spectator server on 127.0.0.1:%s',args.port)
 server.serve_forever()

if __name__=='__main__':
 logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s');main()
