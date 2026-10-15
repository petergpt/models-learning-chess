#!/usr/bin/env python3
"""Publish the entire read-only dashboard to Surge without a ChatGPT backend."""
from pathlib import Path
import argparse,base64,datetime as dt,importlib.util,io,json,logging,netrc,os,re,subprocess,tarfile,tempfile,time,urllib.request

ROOT=Path(__file__).resolve().parent.parent
CONFIG=ROOT/'.operator/surge-publisher-config.json'
STATE=ROOT/'.operator/surge-publisher-status.json'
INTERVAL=65  # Below Surge's unverified-account ceiling of 15 deploys / 15 minutes.

class SurgeRateLimited(Exception):
 def __init__(self,seconds):self.seconds=seconds;super().__init__('Surge domain publishing rate limit')

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path)
 result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result

source=module('chess_public_source',ROOT/'.operator/live-site-publisher.py')
builder=module('chess_surge_builder',ROOT/'surge-site/build.py')

def credential():
 token=os.environ.get('SURGE_TOKEN')
 if token:return token
 try:entry=netrc.netrc().authenticators('surge.surge.sh')
 except (OSError,netrc.NetrcParseError):entry=None
 if not entry or not entry[2]:raise RuntimeError('Surge sign-in is required')
 return entry[2]

def publish(domain,value):
 if not re.fullmatch(r'[a-z0-9][a-z0-9-]*\.surge\.sh',domain):raise ValueError('Invalid Surge domain')
 token=credential();output=builder.build(value)
 files=sorted(path for path in output.iterdir() if path.name in ['index.html','data.json'])
 body=io.BytesIO()
 with tarfile.open(fileobj=body,mode='w:gz') as archive:
  for path in files:archive.add(path,arcname='site/'+path.name,recursive=False)
 authorization=base64.b64encode(('token:'+token).encode()).decode()
 headers={'Authorization':'Basic '+authorization,'Content-Type':'application/gzip','Accept':'application/x-ndjson',
  'version':'0.44.4','file-count':str(len(files)),'project-size':str(sum(p.stat().st_size for p in files)),
  'ssl':'true','message':'Update live chess positions','User-Agent':'chess-spectator/1.0'}
 # curl reads early HTTP rejections before uploading; urllib can hide them behind BrokenPipeError.
 with tempfile.TemporaryDirectory(prefix='surge-upload-',dir=ROOT/'.operator') as temporary:
  temporary=Path(temporary);archive=temporary/'site.tar.gz';archive.write_bytes(body.getvalue())
  header_file=temporary/'headers';response_file=temporary/'response'
  config='\n'.join(['url = '+json.dumps('https://surge.surge.sh/'+domain),'request = "PUT"',
   *['header = '+json.dumps(key+': '+value) for key,value in headers.items()],
   'data-binary = '+json.dumps('@'+str(archive))])+'\n'
  result=subprocess.run(['curl','--config','-','--silent','--show-error','--max-time','60',
   '--dump-header',str(header_file),'--output',str(response_file)],input=config,text=True,capture_output=True,timeout=70)
  response_headers=header_file.read_text() if header_file.exists() else ''
  statuses=re.findall(r'^HTTP/\S+\s+(\d+)',response_headers,re.M)
  status=int(statuses[-1]) if statuses else 0
  if status==429:
   retry=re.search(r'^retry-after:\s*(\d+)',response_headers,re.M|re.I)
   raise SurgeRateLimited(int(retry.group(1)) if retry else 3600)
  if result.returncode or status!=200:raise RuntimeError('Surge upload failed with HTTP '+str(status))
  success=any(json.loads(line).get('type')=='info' for line in response_file.read_text().splitlines() if line.strip())
 if not success:raise RuntimeError('Surge deployment did not complete')
 request=urllib.request.Request('https://'+domain+'/data.json?verify='+str(time.time_ns()),headers={'Cache-Control':'no-cache'})
 with urllib.request.urlopen(request,timeout=20) as response:published=json.load(response)
 if published.get('revision')!=value['revision']:raise RuntimeError('Published data did not match the source')
 return 'https://'+domain

def state(value):
 temp=STATE.with_suffix('.json.tmp');temp.write_text(json.dumps(value,indent=2)+'\n');temp.replace(STATE)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--once',action='store_true');args=parser.parse_args()
 domain=json.loads(CONFIG.read_text())['domain']
 credential()  # Never create a sign-in prompt inside the background service.
 while True:
  saved=json.loads(STATE.read_text()) if STATE.exists() else {}
  retry_at=saved.get('nextAttempt')
  if retry_at:
   delay=dt.datetime.fromisoformat(retry_at).timestamp()-time.time()
   if delay>0:
    if args.once:raise RuntimeError('Surge publishing is rate limited until '+retry_at)
    time.sleep(min(60,delay));continue
  started=time.monotonic()
  try:
   value=source.snapshot(source.thread_states());url=publish(domain,value)
   state({'status':'syncing','url':url,'lastSuccess':source.now(),'revision':value['revision']})
   logging.info('Published live chess dashboard to %s',url)
  except SurgeRateLimited as error:
   retry_at=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(seconds=error.seconds+5)).isoformat()
   state({'status':'rate_limited','url':'https://'+domain,'nextAttempt':retry_at,'error':'Surge domain publishing rate limit'})
   logging.warning('Surge publishing rate limited until %s',retry_at)
   if args.once:raise
  except Exception as error:
   state({'status':'retrying','error':type(error).__name__})
   if args.once:raise
   logging.warning('Surge publication failed: %s',type(error).__name__)
  if args.once:return
  time.sleep(max(1,INTERVAL-(time.monotonic()-started)))

if __name__=='__main__':
 logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s');main()
