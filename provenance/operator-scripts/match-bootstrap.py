#!/usr/bin/env python3
"""Install a precommitted match protocol and identical player interfaces."""
from pathlib import Path
import hashlib
import json
import os
import secrets
import shutil

ROOT=Path(__file__).resolve().parent.parent
MATCH=ROOT/'Matches/Astra vs Opus - 30 games'
SETUP=MATCH/'.operator/setup.json'

def main():
    setup=json.loads(SETUP.read_text())
    protocol_path=MATCH/'protocol.json'
    if not protocol_path.exists():
        protocol={'version':1,'id':'astra-opus-30','games':30,'firstWhite':secrets.choice(['astra','opus']),
            'colors':'alternate; 15 white and 15 black each','position':'standard chess initial position',
            'scoring':{'win':1,'draw':.5,'loss':0},'earlyStop':False,'tie':'drawn match; no sudden-death or speed tiebreak',
            'reasoning':'max for both, explicitly supplied on every turn',
            'context':'each native post-200 conversation branch; original provider context settings retained',
            'learning':'persistent match conversations; own notes and self-reflection allowed between games',
            'assistance':'no engines, automated search/scoring, tablebases, outside chess advice or opponent private material',
            'tools':'identical board/history and legality-only referee; no legal-move menu or evaluations',
            'draws':'stalemate, insufficient material, automatic fivefold/75-move rules; automatically claim completed threefold/50-move positions; mutual agreement',
            'illegalMoves':'third distinct illegal submission at the same position forfeits; transport retries are idempotent',
            'timeControl':'untimed chess; response and elapsed times recorded; provider outages never award chess points',
            'infraRecovery':'preserve the same game and position; retry failed provider requests with backoff; explicit user interruption pauses',
            'safetyLimit':'400 plies: unfinished, no points and match pauses for review; no hidden replacement game',
            'originals':'no original native session, goal, workspace or benchmark ledger is advanced',
            'rating':'head-to-head points are separate from nominal Stockfish Elo',
            'isolation':'separate native threads and player folders under one Unix account; rules and audit, not a security sandbox',
            'sources':{id:{'model':p['modelSelection']['model'],'sourceGames':200,
                'nativeSource':p['nativeId'],'nativeFork':p['forkNativeId'],
                'workspaceManifestSha256':hashlib.sha256(json.dumps(p['sourceWorkspace'],sort_keys=True).encode()).hexdigest(),
                'ledgerSha256':p['sourceLedgerSha256']} for id,p in setup['players'].items()}}
        protocol_path.write_text(json.dumps(protocol,indent=2)+'\n')
    protocol=json.loads(protocol_path.read_text())
    vendor=MATCH/'.referee/vendor/chess';vendor.mkdir(parents=True,exist_ok=True)
    for name in ['__init__.py','py.typed']:
        shutil.copy2(ROOT/'Chess - GPT-6-Astra/.arena/vendor/chess-1.11.2/chess'/name,vendor/name)
    shutil.copy2(ROOT/'Chess - GPT-6-Astra/.arena/vendor/chess-1.11.2/LICENSE.txt',vendor.parent/'LICENSE.txt')
    tokens_path=MATCH/'.referee/tokens.json'
    if tokens_path.exists():tokens=json.loads(tokens_path.read_text())
    else:
        tokens={id:secrets.token_urlsafe(32) for id in setup['players']}
        tokens_path.write_text(json.dumps(tokens));os.chmod(tokens_path,0o600)
    rules='''# Formal 30-game match — user-authorized post-200 branch

The previous 200-game learning run is finished and preserved. This separate conversation and folder are its native branch for a formal match. Your copied `workspace/` contains your own final learning materials; the other player has its own corresponding branch. The old goal's stop-at-200 instruction continues to apply to the original run, and does not prohibit this new match.

Read `GOAL.md` and `MATCH-RULES.md`. Play every move yourself. Max reasoning is selected. Retain your own approach and freedom to reflect; no curriculum or move advice is provided.

- Work only in this player directory. Edit only `workspace/`. Do not read, search, list or modify other players, parent project contents, operator files, private transcripts, credentials, the referee implementation/database, or other benchmark runs. The global memory protection instructions still apply.
- Use `./play` for the match. Do not call the old Stockfish arena or start another benchmark. Do not run chess engines, tablebases, opening explorers, automated search/scoring/evaluation/move selection, other models or outside chess advice. During this entire match use your retained conversation, your own copied notes, your own reasoning and mechanical board/legality helpers only. No web chess research.
- You may retain or create helpers that render a position or check legality mechanically. Do not add a helper that chooses, ranks, scores, searches or recommends moves. Your original notes are yours; do not inspect the opponent's private notes or public operator investigations of either model.
- Read `./play board` at the start of each playing turn. Submit one move using `./play move e2e4`. On acceptance end your assistant turn so the opponent can act. Do not wait, sleep or poll for its reply. The controller returns when it is your turn again. An illegal rejection allows a corrected submission at that same position; the third distinct illegal submission forfeits.
- `./play board` and `./play status` show the neutral board, accepted history, colour, score and whose turn it is. `./play pgn` exports only the current public game. `./play resign`, `./play offer-draw`, `./play accept-draw` act only on your turn. `./play note 'text'` records your own activity in your workspace.
- Do not reset, take back, discard or replace a game. Do not alter `play`, `.match-*`, `AGENTS.md`, `CLAUDE.md`, `GOAL.md` or `MATCH-RULES.md`. Report an infrastructure fault plainly; it pauses the same position and is not a loss. Do not infer results from a timeout or failed request.
- After each game both players receive a separate reflection turn. You can update your own notes freely using the finished public game. Then end your turn; the controller starts the next scheduled game. This is a match between continuing learners, not frozen model weights.
- Never expose private chain-of-thought. An optional move comment is a brief public observation, at most 240 characters. No comment is required.
- At 30 completed games, summarize your measured match result and mark this branch's bounded task complete. Do not begin game 31. Do not resume or modify the original run.
- Use `/home/peter/.local/bin/t3-job -- <command>` for memory-intensive jobs. The shared 56 GiB worker ceiling applies. The play client is lightweight transport and performs no chess analysis.

The players and operator share a Unix account; separate folders are not an adversarial security sandbox. Follow these restrictions even where technically able to bypass them.
'''
    match_rules='''# Match protocol — committed before game one

30 scored games, all played. Each player has 15 games with White and 15 with Black, alternating colours from a recorded random first-colour draw. Every game starts from the normal chess position; there are no selected openings or handicaps. Win = 1, draw = ½, loss = 0. A 15–15 score is a drawn match. No early stop, rapid tiebreak or provider-speed advantage.

Both players use Max reasoning on every turn. Each keeps its own native post-200 conversation and provider context settings, plus its own copied workspace. They may reflect and update their own notes between games, but receive no new outside chess study, engine help, operator tactical advice or opponent private material. The same board/history and legality-only interface is supplied to both. The models have different provider architectures and native context capacities; these are retained and recorded, not claimed to be identical compute budgets.

Standard checkmate, stalemate and insufficient material end the game. Fivefold repetition and the 75-move rule apply automatically. Completed threefold repetition and 50-move positions are claimed automatically for both players. Draw offers require mutual agreement. Three distinct illegal submissions at the same position forfeit; duplicate network retries do not count again. A 400-ply safety limit is recorded as unfinished, awards no points and pauses the match for review.

Chess is untimed. Elapsed times are recorded for viewing and comparison, not used to award wins: API speed, rate limits and network outages are not chess strength. Infrastructure failures preserve the same board and retry with backoff. An explicit user stop pauses. No loss or game is quietly removed or replaced.

The original 200-game ledgers, workspaces, native sessions and completed goals remain unchanged. Match points and games live in a separate referee record and do not alter the Stockfish Elo chart. The neutral referee uses the same pinned chess-rule library, with no Stockfish, search, recommendations or evaluation. Accepted actions are transactional, position-bound and idempotent; an append-only hash chain records the public game events.
'''
    for id,p in setup['players'].items():
        folder=Path(p['folder'])
        for name in ['AGENTS.md','CLAUDE.md']:(folder/name).write_text(rules)
        (folder/'MATCH-RULES.md').write_text(match_rules + '\nFirst White: '+protocol['firstWhite']+'.\n')
        (folder/'GOAL.md').write_text('# Bounded match goal\n\nPlay the authorized 30-game match with your post-200 learned approach. Choose your own moves and reflect on your own games under AGENTS.md and MATCH-RULES.md. Aim to win the match. Continue when the controller supplies your turn; finish and summarize at 30 games. The original 200-game benchmark remains complete.\n')
        (folder/'.match-client.json').write_text(json.dumps({'origin':'http://127.0.0.1:8776','token':tokens[id]}));os.chmod(folder/'.match-client.json',0o600)
        (folder/'play').write_text('''#!/bin/sh
set -eu
player_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 -I "/home/peter/Chess Learning/.operator/match-player.py" --root "$player_root" "$@"
''');os.chmod(folder/'play',0o755)
    (MATCH/'MATCH-RULES.md').write_text(match_rules+'\nFirst White: '+protocol['firstWhite']+'.\n')
    setup['protocolSha256']=hashlib.sha256(protocol_path.read_bytes()).hexdigest()
    setup['firstWhite']=protocol['firstWhite'];setup['status']='prepared'
    SETUP.write_text(json.dumps(setup,indent=2)+'\n')
    print('Protocol committed; first White:',protocol['firstWhite'])
    print('Identical player interfaces installed; no engine copied into the match.')

if __name__=='__main__':main()
