"""Practice isolation and recovery checks, using disposable ledgers only."""
import contextlib
import io
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import test_arena as base
import practice

a=base.a

class PracticeTests(unittest.TestCase):
    setUp=base.ArenaTests.setUp
    tearDown=base.ArenaTests.tearDown

    def command(self,*argv):
        original=a.verify_install;a.verify_install=lambda:None
        try:
            with contextlib.redirect_stdout(io.StringIO()) as output:practice.main(argv,a)
            return output.getvalue()
        finally:a.verify_install=original

    def test_strengths_and_benchmark_isolation(self):
        before=a.read_events();rating=a.rating.estimate(a.games(before))
        for args in [('--skill','0'),('--skill','20'),('--elo','1320'),('--elo','2200'),('--elo','3190')]:
            self.command('start',*args,'--color','black')
            store=practice.Practice(a);g=a.active(store.read())
            self.assertEqual(len(g['moves']),1)
            self.assertTrue(store.board(g).is_valid())
            self.command('end')
        self.assertEqual(a.read_events(),before)
        self.assertEqual(a.rating.estimate(a.games(a.read_events())),rating)
        self.assertFalse(a.LEDGER.exists())
        self.assertEqual(len(a.games(practice.Practice(a).read())),5)

    def test_custom_position_mate_and_pgn(self):
        fen='7k/5Q2/6K1/8/8/8/8/8 w - - 0 1'
        self.command('start','--skill','5','--fen',fen)
        self.command('move','f7g7')
        store=practice.Practice(a);game=a.games(store.read())[-1]
        self.assertEqual(game['end']['reason'],'checkmate')
        record=a.chess.pgn.read_game(io.StringIO(store.pgn(game)))
        self.assertEqual(record.headers['FEN'],fen)
        self.assertEqual(record.end().board().fen(),store.board(game).fen())
        self.assertTrue((store.directory/'games/000001.pgn.gz').exists())

    def test_stop_is_unfinished_and_does_not_delete(self):
        self.command('start','--elo','1800')
        store=practice.Practice(a);before=store.ledger.read_bytes()
        with self.assertRaises(RuntimeError):self.command('start','--skill','1')
        self.command('end','--note','Repeat the drill')
        game=a.games(store.read())[-1]
        self.assertIsNone(game['end']['score'])
        self.assertTrue(store.ledger.read_bytes().startswith(before))
        self.command('start','--skill','1')
        self.assertEqual(a.active(store.read())['start']['game'],2)

    def test_benchmark_blocks_practice_and_replay_is_exact(self):
        events=[]
        a.append(events,'start',game=1,color='white',opponent=a.CONFIG['opponents'][0],snapshot=a.snapshot())
        g=a.active(events)
        with self.assertRaises(RuntimeError):self.command('start','--skill','0')
        a.push(events,g,a.chess.Move.from_uci('e2e4'),'SYNTHETIC_TEST')
        a.push(events,g,a.chess.Move.from_uci('e7e5'),'SYNTHETIC_TEST')
        a.end_game(events,g,'0-1','synthetic_test_resignation')
        before=a.LEDGER.read_bytes()
        self.command('start','--elo','1800','--from-game','1','--ply','2')
        practice_game=a.active(practice.Practice(a).read())
        self.assertEqual(practice_game['start']['initial_fen'],a.board_for(g).fen())
        self.assertEqual(a.LEDGER.read_bytes(),before)

    def test_invalid_inputs_and_illegal_forfeit(self):
        for args in [('--elo','1319'),('--elo','3191'),('--skill','21'),('--skill','-1'),('--skill','1','--fen','8/8/8/8/8/8/8/8 w - - 0 1')]:
            with self.assertRaises(ValueError):self.command('start',*args)
        self.assertFalse(practice.Practice(a).ledger.exists())
        self.command('start','--skill','0')
        for _ in range(3):self.command('move','e2e5')
        game=a.games(practice.Practice(a).read())[-1]
        self.assertEqual(game['end']['reason'],'illegal_move_forfeit')
        self.assertEqual(game['end']['score'],0)

    def test_failed_engine_reply_can_resume(self):
        self.command('start','--skill','0')
        path=a.CONFIG['engine'];a.CONFIG['engine']='does-not-exist'
        try:
            with self.assertRaises(RuntimeError):self.command('move','e2e4')
        finally:a.CONFIG['engine']=path
        store=practice.Practice(a)
        self.assertEqual(len(a.active(store.read())['moves']),1)
        self.command('board')
        self.assertEqual(len(a.active(store.read())['moves']),2)

    def test_practice_corruption_detected(self):
        self.command('start','--skill','0')
        store=practice.Practice(a)
        store.ledger.write_text(store.ledger.read_text().replace('practice-skill-0','practice-skill-1'))
        with self.assertRaises(RuntimeError):store.read()

    def test_cli_isolation_and_benchmark_rotation(self):
        benchmark_command=lambda *args:base.ArenaTests.command(self,*args)
        # Complete a rated skill-0 benchmark, then retain exact stats and rating.
        events=[]
        a.append(events,'start',game=1,color='white',opponent=a.CONFIG['opponents'][1],snapshot=a.snapshot())
        a.end_game(events,a.active(events),'1-0','synthetic_test')
        before=a.LEDGER.read_bytes()
        stats=a.statistics(a.games(a.read_events()))
        rating=a.rating.estimate(a.games(a.read_events()))
        benchmark_command('practice','start','--skill','0')
        with self.assertRaises(RuntimeError):benchmark_command('start')
        benchmark_command('practice','end')
        self.assertEqual(a.LEDGER.read_bytes(),before)
        self.assertEqual(a.statistics(a.games(a.read_events())),stats)
        self.assertEqual(a.rating.estimate(a.games(a.read_events())),rating)
        benchmark_command('start')
        game=a.active(a.read_events())
        self.assertEqual(game['start']['game'],2)
        self.assertEqual(game['start']['color'],'black')
        self.assertEqual(game['start']['opponent'],a.CONFIG['opponents'][0])

if __name__=='__main__':unittest.main(verbosity=2)
