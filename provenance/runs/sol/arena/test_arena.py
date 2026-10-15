#!/usr/bin/env python3
"""Isolated integration checks. No test game is added to the experiment ledger."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import sys

spec = importlib.util.spec_from_file_location('arena', Path(__file__).with_name('arena.py'))
a = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = a
spec.loader.exec_module(a)

class ArenaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='chess-referee-test-')
        self.old = {k:getattr(a,k) for k in ['ROOT','DATA','WORK','LEDGER','EXPORT']}
        a.ROOT = Path(self.temp.name)
        a.DATA = a.ROOT/'data'; a.DATA.mkdir()
        a.WORK = a.ROOT/'workspace'; a.WORK.mkdir()
        a.LEDGER = a.DATA/'ledger.jsonl'
        a.EXPORT = a.ROOT/'exports'; a.EXPORT.mkdir()
        self.nodes = a.CONFIG['nodes_per_move']
        a.CONFIG['nodes_per_move'] = 1000

    def tearDown(self):
        for k,v in self.old.items(): setattr(a,k,v)
        a.CONFIG['nodes_per_move'] = self.nodes
        self.temp.cleanup()

    def start(self, color='white'):
        events = a.read_events()
        a.append(events,'start',game=len(a.games(events))+1,color=color,opponent=a.CONFIG['opponents'][0],
                 model='SYNTHETIC_TEST',snapshot=a.snapshot(),protocol='test')
        return events,a.active(events)

    def command(self,*args):
        old=a.sys.argv
        original=a.verify_install
        a.sys.argv=['play',*args]
        a.verify_install=lambda:None
        try:
            with contextlib.redirect_stdout(io.StringIO()): a.main()
        finally:
            a.sys.argv=old; a.verify_install=original

    def test_benchmark_endpoint_preserves_history_and_excludes_unfinished(self):
        old = a.CONFIG.get('benchmark_game_limit')
        a.CONFIG['benchmark_game_limit'] = 2
        try:
            events, game = self.start()
            a.end_game(events, game, '*', 'synthetic_unfinished')
            self.command('start')
            self.command('resign')
            self.command('start')
            self.command('resign')
            before = a.LEDGER.read_bytes()
            with self.assertRaisesRegex(RuntimeError, 'Benchmark goal complete'):
                self.command('start')
            self.assertEqual(a.LEDGER.read_bytes(), before)
            self.assertEqual(len(a.games(a.read_events())), 3)
            self.assertIsNone(a.active(a.read_events()))
        finally:
            if old is None:
                a.CONFIG.pop('benchmark_game_limit', None)
            else:
                a.CONFIG['benchmark_game_limit'] = old

    def test_real_engine_legal_move_restart_and_resignation(self):
        self.command('start')
        self.command('move','e2e4','--note','Synthetic integration test')
        events=a.read_events(); g=a.active(events)
        self.assertEqual(len(g['moves']),2)
        self.assertEqual(g['moves'][1]['actor'],'stockfish')
        self.assertEqual(g['moves'][0]['reported_tokens'],None)
        self.assertTrue(a.board_for(g).is_valid())
        self.command('resign')
        g=a.games(a.read_events())[-1]
        self.assertEqual(g['end']['score'],0)
        self.assertEqual(a.statistics([g])[0]['losses'],1)
        pgn=a.chess.pgn.read_game(io.StringIO(a.pgn_for(g)))
        self.assertEqual(pgn.end().board().fen(),a.board_for(g).fen())
        self.assertTrue((a.DATA/'games/000001.pgn.gz').exists())

    def test_black_start_and_schedule(self):
        self.command('start'); self.command('resign'); self.command('start')
        g=a.active(a.read_events())
        self.assertEqual(g['start']['color'],'black')
        self.assertEqual(len(g['moves']),1)
        self.assertEqual(a.board_for(g).turn,a.chess.BLACK)
        self.command('resign'); self.command('start')
        self.assertEqual(a.active(a.read_events())['start']['opponent']['id'],'skill-0')

    def test_all_opponent_settings_accept_configuration(self):
        for opponent in a.CONFIG['opponents']:
            events,g=self.start('black')
            g['start']['opponent']=opponent
            a.engine_reply(events,g)
            self.assertEqual(len(g['moves']),1)
            self.assertTrue(a.board_for(g).is_valid())
            a.end_game(events,g,'1-0','synthetic_test_resignation')

    def test_no_discard_and_illegal_forfeit(self):
        self.command('start')
        with self.assertRaises(RuntimeError):self.command('start')
        for _ in range(3): self.command('move','e2e5')
        g=a.games(a.read_events())[-1]
        self.assertEqual(g['end']['reason'],'illegal_move_forfeit')
        self.assertEqual(g['end']['score'],0)
        self.assertEqual(len(g['illegal']),3)
        self.assertIsNone(a.active(a.read_events()))

    def test_checkmate_and_draw(self):
        events,g=self.start()
        for u in ['f2f3','e7e5','g2g4','d8h4']:
            a.push(events,g,a.chess.Move.from_uci(u),'SYNTHETIC_TEST')
        self.assertTrue(a.adjudicate(events,g))
        self.assertEqual(a.games(events)[-1]['end']['result'],'0-1')
        events,g=self.start()
        for u in ['g1f3','g8f6','f3g1','f6g8']*2:
            a.push(events,g,a.chess.Move.from_uci(u),'SYNTHETIC_TEST')
        self.assertTrue(a.adjudicate(events,g))
        self.assertEqual(a.games(events)[-1]['end']['score'],.5)

    def test_move_limit_is_unfinished_not_draw(self):
        events,g=self.start()
        old=a.CONFIG['max_plies']; a.CONFIG['max_plies']=0
        try:self.assertTrue(a.adjudicate(events,g))
        finally:a.CONFIG['max_plies']=old
        self.assertIsNone(a.games(events)[-1]['end']['score'])
        self.assertEqual(a.statistics(a.games(events))[0]['unfinished'],1)

    def test_ledger_corruption_detected(self):
        self.start()
        a.LEDGER.write_text(a.LEDGER.read_text().replace('SYNTHETIC_TEST','tampered'))
        with self.assertRaises(RuntimeError):a.read_events()

    def test_snapshot_dedup_and_changes(self):
        (a.WORK/'notes.md').write_text('First artifact')
        first=a.snapshot()
        self.assertEqual(first,a.snapshot())
        (a.WORK/'notes.md').write_text('Changed artifact')
        self.assertNotEqual(first,a.snapshot())
        self.assertEqual(len(list((a.DATA/'snapshots').glob('*.gz'))),2)

    def test_storage_limit_preserves_ledger(self):
        self.command('start')
        before=a.LEDGER.read_bytes()
        limit=a.CONFIG['storage_limit_bytes'];a.CONFIG['storage_limit_bytes']=0
        try:
            with self.assertRaises(RuntimeError):self.command('move','e2e4')
        finally:a.CONFIG['storage_limit_bytes']=limit
        self.assertEqual(before,a.LEDGER.read_bytes())

    def test_export_script_escaping_and_empty_dashboard(self):
        self.command('export')
        self.assertEqual(len(list(a.EXPORT.glob('*.html'))),1)
        self.command('note','</script><script>alert(1)</script>')
        html=(a.DATA/'dashboard.html').read_text()
        self.assertNotIn('</script><script>alert',html)
        self.assertNotIn('__PAYLOAD__',html)

    def test_engine_error_preserves_move_for_resume(self):
        self.command('start')
        path=a.CONFIG['engine'];a.CONFIG['engine']='does-not-exist'
        try:
            with self.assertRaises(RuntimeError):self.command('move','d2d4')
        finally:a.CONFIG['engine']=path
        self.assertEqual(len(a.active(a.read_events())['moves']),1)
        self.command('board')
        self.assertEqual(len(a.active(a.read_events())['moves']),2)

if __name__=='__main__':
    unittest.main(verbosity=2)
