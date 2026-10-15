"""Behavioural checks for a scored, restartable, neutral head-to-head match."""
from pathlib import Path
import importlib.util
import json
import tempfile
import unittest
import uuid

spec=importlib.util.spec_from_file_location('referee',Path(__file__).with_name('match-referee.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class MatchTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.folder=Path(self.temp.name)
        (self.folder/'protocol.json').write_text(json.dumps({'firstWhite':'astra','games':30}))
        self.ref=m.Referee(self.folder);self.ref.start_game()
    def tearDown(self):self.temp.cleanup()
    def action(self,actor,command='move',uci='e2e4',**kw):
        s=self.ref.state(actor);a={'id':str(uuid.uuid4()),'command':command,'positionToken':s['positionToken']}
        if command=='move':a['uci']=uci
        a.update(kw);return self.ref.act(actor,a),a
    def test_out_of_turn_and_stale_do_not_consume_illegal_attempts(self):
        with self.assertRaises(m.Fault):self.action('opus')
        old=self.ref.state()['positionToken'];self.action('astra')
        with self.assertRaises(m.Fault):self.action('opus',uci='e7e5',positionToken=old)
        self.assertEqual(self.ref.state()['illegalAttempts'],0)
        self.assertEqual(self.ref.state()['ply'],1)
    def test_duplicate_action_after_other_moves_is_idempotent(self):
        result,a=self.action('astra');self.action('opus',uci='e7e5')
        retry=self.ref.act('astra',a)
        self.assertTrue(retry['duplicate']);self.assertEqual(retry['receipt'],result['receipt'])
        self.assertEqual(retry['state']['ply'],2)
        with self.assertRaises(m.Fault):self.ref.act('astra',a|{'uci':'d2d4'})
    def test_illegal_submission_forfeits_at_three_distinct_attempts(self):
        for i in range(3):result,_=self.action('astra',uci='e2e5')
        self.assertFalse(result['receipt']['accepted']);s=self.ref.state()
        self.assertEqual((s['result'],s['reason']),('0-1','illegal_move_forfeit'))
        self.assertEqual(s['score']['points'],{'astra':0,'opus':1})
        self.assertTrue(self.ref.verify()['ok'])
    def test_checkmate_counts_one_game_with_correct_winner(self):
        for actor,uci in [('astra','f2f3'),('opus','e7e5'),('astra','g2g4'),('opus','d8h4')]:self.action(actor,uci=uci)
        s=self.ref.state();self.assertEqual((s['result'],s['reason']),('0-1','checkmate'))
        self.assertEqual(s['score']['completed'],1);self.assertEqual(s['score']['points']['opus'],1)
        self.assertTrue(self.ref.verify()['ok'])
    def test_completed_threefold_is_automatically_claimed(self):
        for _ in range(2):
            for actor,uci in [('astra','g1f3'),('opus','g8f6'),('astra','f3g1'),('opus','f6g8')]:self.action(actor,uci=uci)
        s=self.ref.state();self.assertEqual((s['result'],s['reason']),('1/2-1/2','threefold_repetition'))
        self.assertEqual(s['score']['points'],{'astra':.5,'opus':.5})
    def test_draw_requires_opponent_offer(self):
        with self.assertRaises(m.Fault):self.action('astra',command='accept_draw')
        self.action('astra',command='offer_draw');self.action('astra')
        self.action('opus',command='accept_draw');self.assertEqual(self.ref.state()['result'],'1/2-1/2')
    def test_move_declines_offer(self):
        self.action('astra',command='offer_draw');self.action('astra');self.action('opus',uci='e7e5')
        self.assertIsNone(self.ref.state()['drawOffer'])
    def test_all_30_games_play_and_colours_balance(self):
        colours=[]
        for i in range(1,31):
            if i>1:self.ref.start_game()
            s=self.ref.state();colours.append(s['white']);self.action(s['turn'],command='resign')
        self.assertEqual(colours.count('astra'),15);self.assertEqual(colours.count('opus'),15)
        self.assertEqual(self.ref.state()['status'],'complete')
        self.assertEqual(self.ref.state()['score']['completed'],30)
        with self.assertRaises(m.Fault):self.ref.start_game()
        self.assertTrue(self.ref.verify()['ok'])
    def test_restart_retains_position_and_deduplication(self):
        _,a=self.action('astra');before=self.ref.state();self.ref=m.Referee(self.folder)
        self.assertEqual(self.ref.state(),before);self.assertTrue(self.ref.act('astra',a)['duplicate'])
        self.action('opus',uci='e7e5');self.assertEqual(self.ref.state()['ply'],2)
    def test_public_snapshot_never_exposes_private_material_or_tokens(self):
        self.action('astra');p=self.ref.public();text=json.dumps(p)
        self.assertNotIn('workspace',text);self.assertNotIn('positionToken',text);self.assertNotIn('native',text)
        self.assertEqual(p['games'][0]['uci'],'e2e4');self.assertEqual(p['turn'],'opus')
    def test_public_snapshot_is_consistent_when_a_move_arrives_during_read(self):
        original=self.ref._state;changed=False
        def interleave(db,actor=None):
            nonlocal changed
            state=original(db,actor)
            if actor is None and not changed:
                changed=True
                self.ref.act('astra',{'id':str(uuid.uuid4()),'command':'move','uci':'e2e4','positionToken':state['positionToken']})
            return state
        self.ref._state=interleave
        public=self.ref.public()
        self.assertEqual(public['turn'],'astra')
        self.assertEqual(public['games'][0]['ply'],0)
        self.assertEqual(self.ref.state()['ply'],1)
    def test_hash_chain_and_result_projection_detect_tampering(self):
        self.action('astra',command='resign')
        with self.ref.connect() as db:db.execute("UPDATE games SET result='1-0' WHERE id=1")
        with self.assertRaises(AssertionError):self.ref.verify()
    def test_unknown_fields_and_oversized_comment_are_rejected(self):
        with self.assertRaises(m.Fault):self.action('astra',note='x'*241)
        with self.assertRaises(m.Fault):self.action('astra',fen=m.chess.STARTING_FEN)
        self.assertEqual(self.ref.state()['ply'],0)

if __name__=='__main__':unittest.main()
