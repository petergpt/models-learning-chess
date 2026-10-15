import { DurableObject } from 'cloudflare:workers';
import {ANALYSIS_ID,validAnalysisHistory} from '../surge-site/assets/spectator-outlook-v1.mjs';

const MODELS = ['astra', 'opus', 'sol', 'fable'];
const OPTIONAL_MODELS = ['sol-long-context', 'sol-long-context-max'];
const MAX_BYTES = 1_500_000;
function validMatch(match) {
  if (match == null) return true;
  const keys = ['id','title','status','players','format','score','currentGame','turn','createdAt','startedAt','endedAt','games','eventSequence','ledgerHead','activity','timeline'];
  if (typeof match !== 'object' || Array.isArray(match) || Object.keys(match).some(k => !keys.includes(k))) return false;
  if (match.id !== 'astra-opus-30' || !['ready','playing','between_games','complete','waiting','paused','unfinished'].includes(match.status)) return false;
  if (!match.players || Object.keys(match.players).sort().join(',') !== 'astra,opus') return false;
  for (const id of ['astra','opus']) {
    const p = match.players[id];
    if (!p || Object.keys(p).some(k => !['label','reasoning','sourceGames'].includes(k)) || p.reasoning !== 'max' || p.sourceGames !== 200) return false;
    if (p.label !== (id === 'astra' ? 'GPT-6 Astra' : 'Claude Opus 5.5')) return false;
  }
  if (match.format?.games !== 30 || match.format?.colorsEach !== 15 || !['astra','opus'].includes(match.format.firstWhite)) return false;
  if (!Array.isArray(match.games) || match.games.length > 30 || !match.score || match.score.total !== 30) return false;
  if (match.currentGame !== null && (!Number.isInteger(match.currentGame) || match.currentGame < 1 || match.currentGame > 30)) return false;
  if (match.turn !== null && !['astra','opus'].includes(match.turn)) return false;
  if (!Number.isInteger(match.eventSequence) || !/^[0-9a-f]{64}$/.test(match.ledgerHead)) return false;
  let completed = 0, draws = 0; const points = {astra: 0, opus: 0}, wins = {astra: 0, opus: 0};
  for (let i = 0; i < match.games.length; i++) {
    const g = match.games[i], allowed = ['id','white','black','started','ended','result','reason','uci','san','fen','ply'];
    if (!g || Object.keys(g).some(k => !allowed.includes(k)) || g.id !== i + 1 || !['astra','opus'].includes(g.white) || g.black !== (g.white === 'astra' ? 'opus' : 'astra')) return false;
    const expectedWhite = i % 2 === 0 ? match.format.firstWhite : (match.format.firstWhite === 'astra' ? 'opus' : 'astra');
    if (g.white !== expectedWhite || !Number.isInteger(g.ply) || g.ply < 0 || g.ply > 400) return false;
    if (typeof g.uci !== 'string' || typeof g.san !== 'string' || typeof g.fen !== 'string' || g.fen.length > 100 || g.san.length > 4000 || g.uci.length > 2800) return false;
    if ((g.uci ? g.uci.split(' ').length : 0) !== g.ply || (g.uci && !/^[a-h][1-8][a-h][1-8][qrbn]?(?: [a-h][1-8][a-h][1-8][qrbn]?)*$/.test(g.uci))) return false;
    if (![null,'1-0','0-1','1/2-1/2','*'].includes(g.result) || Boolean(g.ended) !== Boolean(g.result)) return false;
    if (!Number.isFinite(Date.parse(g.started)) || (g.ended && !Number.isFinite(Date.parse(g.ended)))) return false;
    if (i < match.games.length - 1 && !g.ended) return false;
    if (g.result && g.result !== '*') {
      completed++;
      if (g.result === '1/2-1/2') { points.astra += .5; points.opus += .5; draws++; }
      else { const winner = g.result === '1-0' ? g.white : g.black; points[winner]++; wins[winner]++; }
    }
  }
  const last = match.games.at(-1);
  if (match.currentGame !== (last?.id ?? null)) return false;
  const expectedTurn = !last || last.ended ? null : (last.fen.split(' ')[1] === 'w' ? last.white : last.black);
  if (match.turn !== expectedTurn) return false;
  if (match.status === 'complete' && (completed !== 30 || !last?.ended)) return false;
  if (match.activity != null) {
    if (typeof match.activity !== 'object' || Array.isArray(match.activity) || Object.keys(match.activity).sort().join(',') !== 'astra,opus') return false;
    for (const id of ['astra','opus']) {
      const a = match.activity[id];
      if (!a || Object.keys(a).some(k => !['phase','since'].includes(k)) || !['thinking','waiting','reflecting','submitted','ready','retrying','paused','complete','connecting','queued'].includes(a.phase)) return false;
      if (a.since !== null && (typeof a.since !== 'string' || !Number.isFinite(Date.parse(a.since)))) return false;
      if (a.phase === 'thinking' && (match.turn !== id || match.status !== 'playing' || a.since === null)) return false;
    }
  }
  if (match.timeline != null) {
    if (!Array.isArray(match.timeline) || match.timeline.length > 24) return false;
    let previous = 0;
    for (const item of match.timeline) {
      if (!item || Object.keys(item).some(k => !['seq','game','player','ply','san','at','comment'].includes(k))) return false;
      if (!Number.isInteger(item.seq) || item.seq <= previous || item.seq > match.eventSequence || item.game !== match.currentGame || !['astra','opus'].includes(item.player)) return false;
      if (!last || !Number.isInteger(item.ply) || item.ply < 1 || item.ply > last.ply || item.player !== (item.ply % 2 ? last.white : last.black)) return false;
      if (typeof item.san !== 'string' || item.san.length > 16 || item.san !== last.san.split(' ')[item.ply - 1] || !Number.isFinite(Date.parse(item.at))) return false;
      if (item.comment !== undefined && (typeof item.comment !== 'string' || item.comment.length > 240)) return false;
      previous = item.seq;
    }
  }
  return match.score.completed === completed && match.score.draws === draws && ['astra','opus'].every(id => match.score.points?.[id] === points[id] && match.score.wins?.[id] === wins[id]);
}

async function boundedBody(request) {
  if (!request.body) return new Uint8Array();
  const reader = request.body.getReader(), chunks = []; let total = 0;
  try {
    while (true) {
      const {done,value} = await reader.read(); if (done) break;
      total += value.byteLength;
      if (total > MAX_BYTES) { await reader.cancel(); return null; }
      chunks.push(value);
    }
  } finally { reader.releaseLock(); }
  const bytes = new Uint8Array(total); let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk,offset); offset += chunk.byteLength; }
  return bytes;
}
const headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'Cache-Control': 'no-store',
  'X-Content-Type-Options': 'nosniff',
};
const reply = (value, status = 200, extra = {}) =>
  new Response(value == null ? null : JSON.stringify(value), { status, headers: { ...headers, ...extra } });

async function authorized(request, secret) {
  const supplied = request.headers.get('Authorization');
  if (!secret || !supplied?.startsWith('Bearer ')) return false;
  const encoder = new TextEncoder();
  const [expected, actual] = await Promise.all([
    crypto.subtle.digest('SHA-256', encoder.encode(secret)),
    crypto.subtle.digest('SHA-256', encoder.encode(supplied.slice(7))),
  ]);
  const a = new Uint8Array(expected), b = new Uint8Array(actual);
  let difference = 0;
  for (let i = 0; i < a.length; i++) difference |= a[i] ^ b[i];
  return difference === 0;
}

export default {
  async fetch(request, env, ctx) {
    const path = new URL(request.url).pathname;
    const analysis=path.match(/^\/api\/spectator-analysis\/([1-9]|[12][0-9]|30)$/);
    if (analysis) {
      const game=Number(analysis[1]),stub=env.SPECTATOR_ANALYSIS.getByName(ANALYSIS_ID+':astra-opus-30:'+game);
      if(request.method==='PUT') {
        if(!(await authorized(request,env.INGEST_TOKEN)))return reply({error:'Unauthorized'},401);
        const bytes=await boundedBody(request);if(bytes===null || bytes.length>100000)return reply({error:'Analysis too large'},413);
        let value;try{value=JSON.parse(new TextDecoder().decode(bytes));}catch{return reply({error:'Invalid analysis'},400);}
        if(!validAnalysisHistory(value,game))return reply({error:'Invalid analysis'},400);
        const saved=await stub.saveHistory(value);
        return reply(saved,saved.ok?200:409);
      }
      if(!['GET','HEAD'].includes(request.method))return reply({error:'Read only'},405,{Allow:'GET, HEAD'});
      const ply=new URL(request.url).searchParams.get('ply');
      if(ply!==null && (!/^(0|[1-9][0-9]{0,2})$/.test(ply) || Number(ply)>400))return reply({error:'Invalid position'},400);
      const cacheURL=new URL(path,request.url);if(ply!==null)cacheURL.searchParams.set('ply',ply);
      const cacheKey=new Request(cacheURL.href),cache=caches.default;
      const fresh=request.headers.get('Cache-Control')==='no-cache' && await authorized(request,env.INGEST_TOKEN);
      let response=fresh?null:await cache.match(cacheKey);
      if(!response) {
        const value=await stub.getHistory();
        const pending=!value || ply!==null && !value.positions.some(p=>p.ply===Number(ply));
        const control='public, max-age=0, s-maxage='+(pending?2:15)+', must-revalidate';
        const etag=value?'"'+ANALYSIS_ID+':'+game+':'+value.uci.length+':'+value.positions.length+'"':null;
        response=reply(value || {error:'Awaiting analysis'},value?200:404,{'Cache-Control':control,...(etag?{ETag:etag}:{})});
        ctx.waitUntil(cache.put(cacheKey,response.clone()));
      }
      if(response.headers.has('ETag') && request.headers.get('If-None-Match')===response.headers.get('ETag'))return new Response(null,{status:304,headers:response.headers});
      return request.method==='HEAD'?new Response(null,{status:response.status,headers:response.headers}):response;
    }
    if (path === '/api/ingest') {
      if (request.method !== 'PUT') return reply({ error: 'Use PUT' }, 405, { Allow: 'PUT' });
      if (!env.INGEST_TOKEN) return reply({ error: 'Publisher not configured' }, 503);
      if (!(await authorized(request, env.INGEST_TOKEN))) return reply({ error: 'Unauthorized' }, 401);
      if (request.headers.get('Content-Encoding') && request.headers.get('Content-Encoding') !== 'identity')
        return reply({ error: 'Send uncompressed JSON' }, 415);
      if (Number(request.headers.get('Content-Length')) > MAX_BYTES) return reply({ error: 'Snapshot too large' }, 413);
      return env.CHESS_FEED.getByName('live').fetch(request);
    }
    if (['/data', '/data.json', '/health'].includes(path)) {
      if (!['GET', 'HEAD'].includes(request.method)) return reply({ error: 'Read only' }, 405, { Allow: 'GET, HEAD' });
      return env.CHESS_FEED.getByName('live').fetch(request);
    }
    if (['/', '/index.html'].includes(path) && ['GET', 'HEAD'].includes(request.method)) return env.ASSETS.fetch(request);
    return reply({ error: 'Not found' }, 404);
  },
};

// A separate namespace and endpoint: forecasts never enter ChessFeed snapshots.
export class SpectatorAnalysis extends DurableObject {
  async getHistory(){return await this.ctx.storage.get('history') ?? null;}
  async saveHistory(value) {
    const previous=await this.getHistory();
    if(previous) {
      const next=new Map(value.positions.map(p=>[p.ply,p]));
      if(value.white!==previous.white || !(value.uci===previous.uci || !previous.uci || value.uci.startsWith(previous.uci+' '))
        || previous.positions.some(p=>{const n=next.get(p.ply);return !n || n.type!==p.type || n.score!==p.score || n.depth!==p.depth;}))return {ok:false,error:'Existing assessments are immutable'};
    }
    await this.ctx.storage.put('history',value);
    return {ok:true,game:value.game,positions:value.positions.length};
  }
}

export class ChessFeed extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    this.state = ctx;
    this.value = null;
    this.body = null;
    ctx.blockConcurrencyWhile(async () => {
      this.body = await ctx.storage.get('snapshot') ?? null;
      this.value = this.body ? JSON.parse(this.body) : null;
    });
  }

  async fetch(request) {
    if (request.method === 'PUT') {
      const bytes = await boundedBody(request);
      if (bytes === null) return reply({ error: 'Snapshot too large' }, 413);
      let value, body;
      try {
        body = new TextDecoder().decode(bytes);
        value = JSON.parse(body);
        if (!value || !/^[\w:-]{1,160}$/.test(value.revision) || !Number.isFinite(Date.parse(value.updatedAt))) throw Error();
        if (!value.runs || typeof value.runs !== 'object' || Array.isArray(value.runs)) throw Error();
        const ids = Object.keys(value.runs);
        if (MODELS.some(id => !ids.includes(id)) || ids.some(id => ![...MODELS, ...OPTIONAL_MODELS].includes(id))) throw Error();
        for (const id of ids) {
          const run = value.runs[id];
          if (!run || !Array.isArray(run.games) || !run.stats || !run.rating) throw Error();
          if (run.games.some(g => !g.start || typeof g.uci !== 'string' || typeof g.san !== 'string')) throw Error();
        }
        if (!validMatch(value.match)) throw Error();
      } catch {
        return reply({ error: 'Invalid public snapshot' }, 400);
      }
      if (this.value && Date.parse(value.updatedAt) < Date.parse(this.value.updatedAt))
        return reply({ error: 'Older snapshot rejected' }, 409);
      await this.state.storage.put('snapshot', body);
      this.value = value;
      this.body = body;
      return reply({ ok: true, revision: value.revision });
    }
    if (!this.value) return reply({ error: 'Awaiting first snapshot' }, 503);
    const path = new URL(request.url).pathname;
    if (path === '/health') {
      const value = { updatedAt: this.value.updatedAt, revision: this.value.revision };
      return request.method === 'HEAD' ? new Response(null, { headers }) : reply(value);
    }
    const etag = `W/"${this.value.revision}"`;
    const feedHeaders = { ...headers, ETag: etag, 'X-Feed-Updated-At': this.value.updatedAt };
    const validators = (request.headers.get('If-None-Match') ?? '').split(',').map(s => s.trim().replace(/^W\//, ''));
    if (validators.includes('*') || validators.includes(etag.slice(2)))
      return new Response(null, { status: 304, headers: feedHeaders });
    return new Response(request.method === 'HEAD' ? null : this.body, { headers: feedHeaders });
  }
}
