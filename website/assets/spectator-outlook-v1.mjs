// Spectator-only analysis. No player interface, browser uploads or telemetry.
// Hosted history is populated by a separate authenticated spectator analyser.
const ENGINE = '/assets/stockfish/19.0.0/stockfish-19-lite-single.js';
// The same search applies to live, paused, replay and prefetched positions.
export const ANALYSIS_PROFILE = Object.freeze({depth:24,nodes:2000000,movetime:3000,hash:64});
export const SEARCH = `go depth ${ANALYSIS_PROFILE.depth} nodes ${ANALYSIS_PROFILE.nodes} movetime ${ANALYSIS_PROFILE.movetime}`;
export const ANALYSIS_ID = 'sf19-lite-d24-n2m-t3000-h64-v1';

export function validAnalysisHistory(value, game = value?.game) {
  if (!value || typeof value !== 'object' || Array.isArray(value) || Object.keys(value).some(k=>!['profile','game','white','uci','positions','updatedAt'].includes(k))) return false;
  if (value.profile!==ANALYSIS_ID || value.game!==game || !Number.isInteger(game) || game<1 || game>30 || !['astra','opus'].includes(value.white)) return false;
  if (typeof value.uci!=='string' || value.uci.length>2800 || (value.uci && !/^[a-h][1-8][a-h][1-8][qrbn]?(?: [a-h][1-8][a-h][1-8][qrbn]?)*$/.test(value.uci))) return false;
  const length=value.uci?value.uci.split(' ').length:0;
  if (length>400 || !Array.isArray(value.positions) || value.positions.length>length+1 || !Number.isFinite(Date.parse(value.updatedAt))) return false;
  const seen=new Set();
  return value.positions.every(p=>{
    if (!p || Object.keys(p).some(k=>!['ply','type','score','depth'].includes(k)) || !Number.isInteger(p.ply) || p.ply<0 || p.ply>length || seen.has(p.ply)) return false;
    seen.add(p.ply);
    return ['cp','mate'].includes(p.type) && Number.isInteger(p.score) && Math.abs(p.score)<=(p.type==='mate'?400:100000) && Number.isInteger(p.depth) && p.depth>=0 && p.depth<=128;
  });
}

// Public spectator cache only. It never reads or writes the neutral player feed.
export class CachedSpectatorOutlook {
  constructor({onUpdate,fetcher=(...args)=>fetch(...args),setTimer=(fn,ms)=>setTimeout(fn,ms),clearTimer=id=>clearTimeout(id),now=()=>Date.now()}) {
    Object.assign(this,{onUpdate,fetcher,setTimer,clearTimer,now});
    this.cache=new Map();this.histories=new Map();this.loaded=new Map();this.pending=new Map();this.wanted=null;this.timer=null;
  }
  setPosition(position) {
    this.wanted=position?{...position}:null;
    if (!position) {this.suspend();return;}
    const finished=finishedOutlook(position),result=finished || this.cache.get(position.key);
    if (finished) this.cache.set(position.key,finished);
    this.onUpdate(result?{...result,key:position.key,state:'ready'}:{key:position.key,state:'analysing'});
  }
  warmHistory(history) {
    this.histories.set(history.game,{...history,moves:[...history.moves]});
    this.sync(history.game);
  }
  async sync(game) {
    const history=this.histories.get(game);if (!history || this.pending.has(game)) return;
    const uci=history.moves.join(' '),loaded=this.loaded.get(game);
    if (loaded && (loaded.complete && loaded.uci===uci || loaded.requestedUci===uci && this.now()-loaded.at<this.refreshInterval(game))) {this.schedule();return;}
    const requested={...loaded,requestedUci:uci,attempts:loaded?.requestedUci===uci?loaded.attempts+1:1,at:this.now()};
    this.loaded.set(game,requested);
    // A new move gets its own shared edge cache, instead of inheriting an old
    // board's fifteen-second cache. Pending assessments are cached briefly.
    const task=this.fetcher('/api/spectator-analysis/'+game+'?ply='+history.moves.length,{headers:loaded?.etag?{'If-None-Match':loaded.etag}:{},signal:AbortSignal.timeout(15000)});
    this.pending.set(game,task);
    try {
      const response=await task;
      if (response.status===304) return;
      if (!response.ok) return;
      const value=await response.json();
      const current=this.histories.get(game),actual=current.moves.join(' ');
      if (!validAnalysisHistory(value,game) || value.white!==current.white || !(actual===value.uci || !actual || !value.uci || actual.startsWith(value.uci+' ') || value.uci.startsWith(actual+' '))) return;
      const moves=value.uci?value.uci.split(' '):[];
      for (const p of value.positions) {
        // Analysis may arrive before the neutral board feed. Keep every valid
        // position in this spectator cache; only the wanted key is displayed.
        const prefix=moves.slice(0,p.ply).join(' '),key=`${game}:${value.white}:${prefix}`;
        if(this.cache.has(key))continue;
        const result=positionAssessment(`info depth ${p.depth} score ${p.type} ${p.score}`,{white:value.white,ply:p.ply});
        if(result)this.cache.set(key,result);
      }
      this.loaded.set(game,{...requested,uci:value.uci,complete:value.positions.length===moves.length+1,etag:response.headers.get('ETag'),at:this.now()});
      const target=this.wanted,result=target && (finishedOutlook(target)||this.cache.get(target.key));
      if(result)this.onUpdate({...result,key:target.key,state:'ready'});
    } catch { /* A missing assessment stays hidden; transport never waits. */ }
    finally {this.pending.delete(game);this.schedule();}
  }
  refreshInterval(game) {
    const target=this.wanted,loaded=this.loaded.get(game);
    return target?.game===game && !finishedOutlook(target) && !this.cache.has(target.key) && (loaded?.attempts || 0)<5 ? 3000 : 15000;
  }
  schedule() {
    this.clearTimer(this.timer);this.timer=null;
    if(!this.wanted)return;
    const game=this.wanted.game,history=this.histories.get(game),loaded=this.loaded.get(game);
    if(history && !(loaded?.complete && loaded.uci===history.moves.join(' '))) {
      // Repeated renders must not postpone an already scheduled refresh. A move
      // that arrives during a request is fetched as soon as that request ends.
      const delay=loaded?.requestedUci===history.moves.join(' ')?Math.max(0,this.refreshInterval(game)-(this.now()-loaded.at)):0;
      this.timer=this.setTimer(()=>{this.timer=null;this.sync(game);},delay);
    }
  }
  suspend(){this.clearTimer(this.timer);this.timer=null;this.wanted=null;}
}

export function roundChances(values) {
  const total = values.reduce((sum, value) => sum + value, 0);
  if (values.length !== 3 || !values.every(v => Number.isFinite(v) && v >= 0) || !total) return null;
  const exact = values.map(v => v / total * 100), rounded = exact.map(Math.floor);
  const order = exact.map((v, i) => ({i, remainder: v - rounded[i]})).sort((a, b) => b.remainder - a.remainder || a.i - b.i);
  for (let i = 0, left = 100 - rounded.reduce((a, b) => a + b, 0); i < left; i++) rounded[order[i].i]++;
  return rounded;
}

export function positionAssessment(line, position) {
  if (!/^info\s/.test(line) || /\b(?:upperbound|lowerbound)\b/.test(line)) return null;
  const score = line.match(/\bscore\s+(cp|mate)\s+(-?\d+)\b/);
  if (!score || !['astra', 'opus'].includes(position.white)) return null;
  const depth = Number(line.match(/\bdepth\s+(\d+)/)?.[1] || 0);
  const astraToMove = (position.ply % 2 === 0) === (position.white === 'astra');
  const value = Number(score[2]), astraValue = astraToMove ? value : -value;
  if (score[1] === 'mate') {
    const leader = value > 0 ? (astraToMove ? 'astra' : 'opus') : (astraToMove ? 'opus' : 'astra');
    return {share: leader === 'astra' ? [100, 0] : [0, 100], leader,
      label: (leader === 'astra' ? 'Astra' : 'Opus') + (value ? ': checkmate in ' + Math.abs(value) : ' wins by checkmate'), depth};
  }
  // Use the conventional Lichess evaluation-bar scale, without calling its width
  // a calibrated probability for these models: https://lichess.org/page/accuracy.
  const astraShare = 100 / (1 + Math.exp(-.00368208 * Math.max(-1000, Math.min(1000, astraValue))));
  const leader = Math.abs(astraValue) <= 20 ? null : astraValue > 0 ? 'astra' : 'opus';
  return {share: [astraShare, 100 - astraShare], leader, cp: astraValue, depth,
    label: leader ? (leader === 'astra' ? 'Astra' : 'Opus') + ' +' + (Math.abs(astraValue) / 100).toFixed(1) : 'Equal'};
}

export function parseOutlook(line, position) {
  const assessment = positionAssessment(line, position);
  if (!assessment) return null;
  const match = line.match(/\bwdl\s+(\d+)\s+(\d+)\s+(\d+)\b/);
  if (!match) return assessment;
  const numbers = match.slice(1).map(Number);
  if (numbers.some(n => n > 1000) || !numbers.reduce((a, b) => a + b, 0)) return assessment;
  const [win, draw, loss] = numbers;
  const whiteWins = position.ply % 2 ? loss : win, blackWins = position.ply % 2 ? win : loss;
  const values = position.white === 'astra' ? [whiteWins, draw, blackWins] : [blackWins, draw, whiteWins];
  const percentages = roundChances(values);
  return {...assessment, percentages};
}

export function finishedOutlook(position) {
  if (position.result === '1/2-1/2') return {share: [50, 50], leader: null, label: 'Draw', percentages: [0, 100, 0], finished: true};
  if (!['1-0', '0-1'].includes(position.result)) return null;
  const astraWins = (position.result === '1-0') === (position.white === 'astra');
  return {share: astraWins ? [100, 0] : [0, 100], leader: astraWins ? 'astra' : 'opus', label: astraWins ? 'Astra wins' : 'Opus wins',
    percentages: astraWins ? [100, 0, 0] : [0, 0, 100], finished: true};
}

export class SpectatorOutlook {
  constructor({onUpdate, createWorker = url => new Worker(url),
    setTimer = (fn, ms) => setTimeout(fn, ms), clearTimer = id => clearTimeout(id)}) {
    Object.assign(this, {onUpdate, createWorker, setTimer, clearTimer});
    this.cache = new Map(); this.worker = null; this.ready = false; this.generation = 0;
    this.wanted = null; this.active = null; this.debounce = null; this.watchdog = null;
    this.lastGame = null; this.failed = false; this.warm = []; this.historyKey = null;
    this.direction = -1; this.prepared = new Map(); this.priority = [];
  }

  // Prepare a replay frame without changing the currently displayed position.
  // The caller commits its board and cached assessment together when ready.
  preparePosition(position) {
    const finished = finishedOutlook(position);
    if (finished) { this.remember(position.key, finished); return Promise.resolve(true); }
    if (this.cache.has(position.key)) return Promise.resolve(true);
    if (this.failed || !this.wanted) return Promise.resolve(false);
    return new Promise(resolve => {
      const waiting = this.prepared.get(position.key);
      if (waiting) waiting.push(resolve);
      else { this.prepared.set(position.key, [resolve]); this.priority.push({...position}); }
      if (!this.worker) this.startWorker();
      this.pump();
    });
  }

  setPosition(position) {
    if (!position) { this.suspend(); return; }
    const same = this.wanted?.key === position.key;
    const finished = finishedOutlook(position);
    const cached = this.cache.get(position.key);
    if (!same && this.wanted?.game === position.game && this.wanted.ply !== position.ply) {
      this.direction = Math.sign(position.ply - this.wanted.ply);
    }
    if (same && !finished && (this.worker || this.cache.has(position.key) || this.failed)) {
      this.wanted = {...position}; this.pump(); return;
    }
    this.wanted = {...position}; this.failed = false;
    this.clearTimer(this.debounce);
    this.debounce = null;
    if (this.active && !this.active.cancelled) {
      if (!finished && this.active.key === position.key) {
        // A prefetched neighbour is now visible: finish it without restarting.
        this.active.background = false;
      } else if (this.active.game === position.game && this.active.white === position.white) {
        // Playback never waits for analysis. Finish this search in the background
        // so fast-moving frames cannot repeatedly cancel it before it is cached.
        this.active.background = true;
      } else {
        this.active.cancelled = true;
        this.worker?.postMessage('stop');
      }
    }
    if (finished) { this.remember(position.key, finished); this.publish(finished, position); return; }
    if (cached) this.publish(cached, position);
    else this.onUpdate({key: position.key, state: 'analysing'});
    this.debounce = this.setTimer(() => {
      this.debounce = null;
      if (!this.worker) this.startWorker(); else this.pump();
    }, position.replaying ? 20 : 120);
  }

  warmHistory({game, white, moves}) {
    const historyKey = `${game}:${white}:${moves.join(' ')}`;
    if (historyKey === this.historyKey) { this.prioritizeWarm();this.pump();return; }
    this.historyKey = historyKey;
    this.warm = Array.from({length: Math.min(400, moves.length) + 1}, (_, ply) => {
      const history = moves.slice(0, ply).join(' ');
      return {key: `${game}:${white}:${history}`, game, white, moves: history, ply};
    }).filter(position => !this.cache.has(position.key) && position.key !== this.wanted?.key);
    this.prioritizeWarm();
    // A completed board also prepares neighbouring replay positions on first load.
    if (!this.worker && !this.failed && this.warm.length && this.cache.has(this.wanted?.key)) this.startWorker();
    this.pump();
  }

  prioritizeWarm() {
    const ply=this.wanted?.ply;
    if (ply == null) return;
    const ahead=position=>(position.ply-ply)*this.direction>0?0:1;
    this.warm.sort((a,b)=>Math.abs(a.ply-ply)-Math.abs(b.ply-ply)||ahead(a)-ahead(b)||a.ply-b.ply);
  }

  startWorker() {
    if (!this.wanted) return;
    try {
      const generation = ++this.generation;
      this.worker = this.createWorker(ENGINE); this.ready = false;
      this.worker.onmessage = event => {
        if (generation !== this.generation) return;
        for (const line of String(event.data).split('\n')) this.receive(line.trim());
      };
      this.worker.onerror = () => { if (generation === this.generation) this.fail(); };
      this.armTimeout(20000);
      this.worker.postMessage('uci');
    } catch { this.fail(); }
  }

  receive(line) {
    if (line === 'uciok') {
      for (const command of ['setoption name Hash value '+ANALYSIS_PROFILE.hash, 'setoption name MultiPV value 1', 'setoption name UCI_ShowWDL value true', 'isready']) this.worker.postMessage(command);
    } else if (line === 'readyok') {
      this.ready = true; this.clearTimer(this.watchdog); this.watchdog = null; this.pump();
    } else if (/\bCRITICAL ERROR\b/.test(line)) {
      this.fail();
    } else if (line.startsWith('bestmove ')) {
      const active = this.active;
      this.active = null; this.clearTimer(this.watchdog); this.watchdog = null;
      if (active && !active.cancelled) {
        if (active.result) { this.publish(this.remember(active.key, active.result), active); }
        else if (!active.background) { this.fail(); return; }
      }
      this.pump();
    } else if (this.active && !this.active.cancelled) {
      const result = parseOutlook(line, this.active);
      if (result && result.depth >= (this.active.result?.depth || 0)) this.active.result = result;
    }
  }

  pump() {
    if (!this.ready || this.active || this.debounce != null || !this.wanted) return;
    const cached = this.cache.get(this.wanted.key);
    let position = this.wanted, background = false;
    if (cached) {
      do { position = this.priority.shift() || this.warm.shift(); } while (position && this.cache.has(position.key));
      if (!position) return;
      background = true;
    }
    const moves = position.moves || '';
    if (!['astra', 'opus'].includes(position.white) || !Number.isInteger(position.ply) || position.ply < 0 || position.ply > 400
        || (moves && !/^[a-h][1-8][a-h][1-8][qrbn]?(?: [a-h][1-8][a-h][1-8][qrbn]?)*$/.test(moves))
        || (moves ? moves.split(' ').length : 0) !== position.ply) { this.fail(); return; }
    this.active = {...position, result: null, cancelled: false, background};
    if (this.lastGame !== position.game) { this.worker.postMessage('ucinewgame'); this.lastGame = position.game; }
    // Replay the actual move history: preserve castling, en passant and repetitions.
    this.worker.postMessage('position startpos' + (moves ? ' moves ' + moves : ''));
    this.armTimeout(15000);
    this.worker.postMessage(SEARCH);
  }

  publish(result, position) {
    if (position.key === this.wanted?.key) this.onUpdate({...result, key: position.key, state: 'ready'});
  }

  remember(key, result) {
    // Keep a completed assessment stable on repeat visits. Actual game results
    // still override an assessment when the game finishes at the same board.
    if (this.cache.has(key) && !result.finished) return this.cache.get(key);
    this.cache.set(key, result);
    if (this.cache.size > 512) this.cache.delete(this.cache.keys().next().value);
    for (const resolve of this.prepared.get(key) || []) resolve(true);
    this.prepared.delete(key);
    return result;
  }

  clearPreparation() {
    for (const waiting of this.prepared.values()) for (const resolve of waiting) resolve(false);
    this.prepared.clear(); this.priority = [];
  }

  armTimeout(ms) {
    this.clearTimer(this.watchdog); this.watchdog = this.setTimer(() => this.fail(), ms);
  }

  fail() {
    const key = this.wanted?.key;
    this.stopWorker(); this.clearPreparation(); this.failed = true;
    if (key) {
      const cached = this.cache.get(key);
      if (cached) this.publish(cached, this.wanted); else this.onUpdate({key, state: 'unavailable'});
    }
  }

  stopWorker() {
    this.clearTimer(this.debounce); this.clearTimer(this.watchdog);
    this.debounce = this.watchdog = null;
    this.worker?.terminate(); this.worker = null; this.active = null; this.ready = false;
    this.lastGame = null; this.generation++;
  }

  suspend() { this.stopWorker(); this.clearPreparation(); this.wanted = null; this.failed = false; this.warm = []; this.historyKey = null; }
}
