import importlib.util
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('rating',Path(__file__).with_name('rating.py'))
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

def observations(scores,anchor=1500):
    return [dict(anchor=anchor,score=s) for s in scores]

def game(n,score,setting='elo-1800-setting'):
    return dict(start=dict(game=n,opponent={'id':setting}),
                end=dict(score=score,timestamp=f'test-{n}'))

class RatingTests(unittest.TestCase):
    def test_no_results_do_not_display_prior_as_rating(self):
        self.assertIsNone(r.estimate([])['estimate'])

    def test_unrated_target_is_not_assigned_invented_elo(self):
        self.assertIsNone(r.estimate([game(1,0,'full-strength')])['estimate'])

    def test_one_win_has_wide_finite_interval(self):
        result=r.posterior(observations([1]))
        self.assertGreater(result['estimate'],1500)
        self.assertGreater(result['upper']-result['lower'],1500)
        self.assertLess(result['grid_edge_mass'],1e-6)

    def test_one_loss_mirrors_one_win(self):
        win=r.posterior(observations([1]));loss=r.posterior(observations([0]))
        self.assertAlmostEqual(win['estimate']+loss['estimate'],3000,delta=10)
        self.assertAlmostEqual(win['lower']+loss['upper'],3000,delta=10)

    def test_draws_and_balanced_decisive_results_center_on_anchor(self):
        for scores,width_limit in [([.5]*20,2000),([0,1]*10,600)]:
            out=r.posterior(observations(scores))
            self.assertAlmostEqual(out['estimate'],1500,delta=10)
            # All draws can also be explained by high draw propensity, so are
            # less informative about strength than a balanced decisive sample.
            self.assertLess(out['upper']-out['lower'],width_limit)

    def test_stronger_opponent_gives_higher_rating(self):
        low=r.posterior(observations([0,1]*10,1320))
        high=r.posterior(observations([0,1]*10,1800))
        self.assertGreater(high['estimate'],low['estimate']+350)

    def test_more_balanced_games_narrow_interval(self):
        small=r.posterior(observations([0,1]))
        big=r.posterior(observations([0,1]*20))
        self.assertLess(big['upper']-big['lower'],small['upper']-small['lower'])

    def test_cache_and_history_have_no_future_leakage(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'cache.json'
            first=r.estimate([game(1,1)],path)
            again=r.estimate([game(1,1)],path)
            self.assertEqual(first,again)
            second=r.estimate([game(1,1),game(2,0)],path)
            self.assertEqual(first['history'][0],second['history'][0])
            self.assertLess(second['estimate'],first['estimate'])

    def test_unfinished_game_is_excluded(self):
        self.assertIsNone(r.estimate([game(1,None)])['estimate'])

if __name__=='__main__':unittest.main(verbosity=2)
