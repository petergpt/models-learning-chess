"""Provisional Bayesian engine-relative rating; observes results only.

Bradley-Terry-Davidson W/D/L likelihood with unknown draw propensity.
Nominal anchors are configuration labels, not human rating calibration.
"""
import collections
import hashlib
import json
import math
from pathlib import Path

VERSION = 'nominal-stockfish-davidson-v1'
ANCHORS = {'skill-0': 1320, 'elo-1800-setting': 1800}
PRIOR_MEAN = 1500
PRIOR_SD = 800
WINDOW = 50
RATINGS = range(-2500, 6501, 10)
# Uniform prior on equally matched draw probability, integrated by midpoint grid.
DRAW_PROBABILITIES = [(i + .5) / 40 for i in range(40)]

def logsumexp(values):
    top = max(values)
    return top + math.log(sum(math.exp(v-top) for v in values))

def posterior(observations):
    counts = collections.Counter((o['anchor'], o['score']) for o in observations)
    by_anchor = {}
    for (anchor, score), count in counts.items():
        if score not in (0, .5, 1): raise ValueError('Unexpected game score')
        by_anchor.setdefault(anchor, [0, 0, 0])[{0:0, .5:1, 1:2}[score]] += count
    density = []
    for rating in RATINGS:
        log_prior = -.5*((rating-PRIOR_MEAN)/PRIOR_SD)**2
        margins = [(math.log(10)*(rating-anchor)/800, count) for anchor,count in by_anchor.items()]
        draw_terms = []
        for draw in DRAW_PROBABILITIES:
            log_nu = math.log(2*draw/(1-draw))
            likelihood = 0.
            for margin,(losses,draws,wins) in margins:
                denominator = logsumexp([margin, -margin, log_nu])
                likelihood += wins*(margin-denominator) + losses*(-margin-denominator) + draws*(log_nu-denominator)
            draw_terms.append(likelihood)
        density.append(log_prior + logsumexp(draw_terms)-math.log(len(draw_terms)))
    normalizer = logsumexp(density)
    probabilities = [math.exp(x-normalizer) for x in density]
    def quantile(q):
        total=0.
        for rating,p in zip(RATINGS,probabilities):
            total += p
            if total >= q:return rating
        return RATINGS[-1]
    return dict(estimate=quantile(.5), lower=quantile(.025), upper=quantile(.975),
                grid_edge_mass=sum(probabilities[:5]+probabilities[-5:]))

def estimate(games, cache_path=None):
    completed=[g for g in games if g['end'] and g['end']['score'] is not None]
    observations=[]
    for g in completed:
        setting=g['start']['opponent']['id']
        if setting in ANCHORS:
            observations.append(dict(game=g['start']['game'],timestamp=g['end']['timestamp'],
                                     anchor=ANCHORS[setting],score=g['end']['score']))
    signature=hashlib.sha256(json.dumps([VERSION, observations, len(completed),
                                      sum(bool(g['end']) and g['end']['score'] is None for g in games)],sort_keys=True).encode()).hexdigest()
    cached={}
    if cache_path and cache_path.exists():
        try:cached=json.loads(cache_path.read_text())
        except (ValueError,OSError):pass
        if cached.get('signature')==signature:return cached['rating']
    result=dict(version=VERSION, label='Provisional engine-relative Elo',
                estimate=None, lower=None, upper=None, interval_level=.95,
                interval_type='Bayesian equal-tail credible interval',
                rated_games_total=len(observations), rated_games_in_window=min(WINDOW,len(observations)),
                excluded_uncalibrated=len(completed)-len(observations), window=WINDOW,
                anchors=ANCHORS, prior=dict(distribution='normal',mean=PRIOR_MEAN,sd=PRIOR_SD),
                draw_prior='Uniform(0,1) on equal-strength draw probability; 40 midpoint bins',
                uncertainty_note='Conditional on nominal anchors and model assumptions; excludes systematic anchor calibration error. Not FIDE or platform Elo.',
                small_sample=len(observations)<20, history=[])
    # Retrospective points use only the games available at each point, never future results.
    previous=cached.get('rating',{}) if cached.get('rating',{}).get('version')==VERSION else {}
    old_history={point['game']:point for point in previous.get('history',[])}
    for i in range(max(0,len(observations)-200),len(observations)):
        obs=observations[i]
        point=old_history.get(obs['game'])
        window=observations[max(0,i+1-WINDOW):i+1]
        point_key=hashlib.sha256(json.dumps(window,sort_keys=True).encode()).hexdigest()
        if not point or point.get('window_hash')!=point_key:
            point=dict(game=obs['game'],timestamp=obs['timestamp'],rated_games=i+1,
                       window_hash=point_key,**posterior(window))
        result['history'].append(point)
    if result['history']:
        last=result['history'][-1]
        for key in ('estimate','lower','upper','grid_edge_mass'):result[key]=last[key]
    if cache_path:
        tmp=cache_path.with_suffix('.tmp')
        tmp.write_text(json.dumps(dict(signature=signature,rating=result),indent=2)+'\n')
        tmp.replace(cache_path)
    return result
