"""Check dispatch idempotency, explicit Max settings and user-stop handling."""
from pathlib import Path
from contextlib import contextmanager
import importlib.util
import json
import tempfile
import unittest
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('controller',Path(__file__).with_name('match-controller.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class FakeReferee:
    def __init__(self):
        self.values={'status':'waiting'};self.events=[]
    @contextmanager
    def connect(self):yield self
    def meta(self,db,key):return self.values.get(key)
    def set_meta(self,db,key,value):self.values[key]=value
    def current(self,db):return {'ended':None}
    def _state(self,db):return {'game':12,'ply':104}
    def event(self,db,kind,game,actor,payload):self.events.append((kind,game,actor,payload))

class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.state_path=Path(self.temp.name)/'state.json'
        self.patch=patch.object(m,'STATE',self.state_path);self.patch.start()
        self.c=object.__new__(m.Controller)
        self.c.state={'status':'active','slots':{},'ownMessageIds':[],'dispatches':0}
        self.c.ref=FakeReferee()
        setup=json.loads(m.SETUP.read_text());self.c.players=setup['players']
        self.thread={'messages':[],'session':{'status':'stopped'},'latestTurn':None}
    def tearDown(self):self.patch.stop();self.temp.cleanup()
    def test_each_provider_receives_explicit_max_on_every_turn(self):
        with patch.object(m,'request',return_value={}) as request:
            for id in ['astra','opus']:
                self.c.dispatch(id,'move:1:'+id,'Your turn.',self.thread)
                command=request.call_args.args[1]
                options={o['id']:o['value'] for o in command['modelSelection']['options']}
                self.assertEqual(options['reasoningEffort' if id=='astra' else 'effort'],'max')
                self.assertEqual(command['threadId'],self.c.players[id]['threadId'])
    def test_uncertain_dispatch_reuses_exact_command_and_message(self):
        with patch.object(m,'request',side_effect=TimeoutError):
            with self.assertRaises(TimeoutError):self.c.dispatch('astra','move:1:0','Your turn.',self.thread)
        saved=json.loads(self.state_path.read_text())['slots']['move:1:0']['command']
        with patch.object(m,'request',return_value={}) as request:
            self.c.dispatch('astra','move:1:0','Your turn.',self.thread)
            self.assertEqual(request.call_args.args[1],saved)
        self.assertEqual(len(self.c.state['ownMessageIds']),1)
    def test_acknowledged_dispatch_is_not_repeated_on_restart(self):
        with patch.object(m,'request',return_value={}) as request:
            self.c.dispatch('astra','move:1:0','Your turn.',self.thread)
            self.c.state=json.loads(self.state_path.read_text())
            self.c.dispatch('astra','move:1:0','Your turn.',self.thread)
            self.assertEqual(request.call_count,1)
    def test_interrupt_and_foreign_user_stop_pause(self):
        self.assertTrue(self.c.stopped({'latestTurn':{'state':'interrupted'}}))
        self.assertTrue(self.c.stopped({'messages':[{'id':'external','role':'user','text':'Please pause the match.'}]}))
        self.c.state['ownMessageIds'].append('own')
        self.assertFalse(self.c.stopped({'messages':[{'id':'own','role':'user','text':'Stop playing at 30 games.'}]}))
    def test_provider_error_does_not_count_as_completed(self):
        with patch.object(m,'request',return_value={}):record=self.c.dispatch('opus','move:1:0','Your turn.',self.thread)
        t={'latestTurn':{'state':'error'},'session':{'status':'error'},'messages':[{'id':record['command']['message']['messageId']}]}
        self.assertFalse(self.c.completed(record,t))
    def test_busy_provider_is_not_idle(self):
        self.assertFalse(self.c.idle({'session':{'status':'running'},'latestTurn':{'state':'running'}}))
    def test_manual_continue_without_action_restores_playing_and_redispatches(self):
        with patch.object(m,'request',return_value={}):
            self.c.dispatch('astra','move:12:104:astra','Your turn.',self.thread)
        self.c.state['status']='waiting'
        manual={'session':{'status':'ready'},'latestTurn':{'state':'completed'},
                'messages':[{'id':'manual','role':'user','text':'Continue'}]}
        with patch.object(m,'request',return_value={}) as request:
            self.c.retry('astra','move:12:104:astra','Your turn.',manual)
        self.assertEqual(self.c.ref.values['status'],'playing')
        self.assertEqual(self.c.state['status'],'active')
        self.assertEqual(request.call_count,1)
        self.assertEqual(self.c.state['slots']['move:12:104:astra']['emptyCompletions'],1)
        self.assertEqual(self.c.ref.events[0][0],'infrastructure_resume')
        self.assertNotIn('e4d4',request.call_args.args[1]['message']['text'])
    def test_busy_manual_continue_is_not_redispatched(self):
        with patch.object(m,'request',return_value={}):
            self.c.dispatch('astra','move:12:104:astra','Your turn.',self.thread)
        busy={'session':{'status':'running'},'latestTurn':{'state':'running'},'messages':[]}
        with patch.object(m,'request',return_value={}) as request:
            self.c.retry('astra','move:12:104:astra','Your turn.',busy)
        self.assertEqual(request.call_count,0)
        self.assertEqual(self.c.ref.values['status'],'waiting')
    def test_three_empty_turns_still_pause_without_forfeit(self):
        with patch.object(m,'request',return_value={}):
            self.c.dispatch('astra','move:12:104:astra','Your turn.',self.thread)
        self.c.state['slots']['move:12:104:astra']['emptyCompletions']=3
        manual={'session':{'status':'ready'},'latestTurn':{'state':'completed'},'messages':[]}
        with patch.object(m,'request',return_value={}) as request:
            self.c.retry('astra','move:12:104:astra','Your turn.',manual)
        self.assertEqual(request.call_count,0)
        self.assertEqual(self.c.state['status'],'paused')
        self.assertTrue(all(event[0]!='game_ended' for event in self.c.ref.events))

if __name__=='__main__':unittest.main()
