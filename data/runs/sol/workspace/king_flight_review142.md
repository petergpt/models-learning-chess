# Game 142: released guards and a rook mate

Trial 238, Black against skill-0: loss by 51.Re6#, 101 plies, zero illegal submissions. Referee result seq 11613, timestamp 2026-10-09T05:18:59.972828+00:00. Completed PGN and status were read directly. Cumulative: 142 scored, 39 wins / 7 draws / 96 losses. Full strength 0/0/48; skill-0 32/4/12; nominal 1800 7/3/36. Provisional engine-relative Elo 1540, conditional 95% Bayesian interval [1410,1660], latest 50 of 94 rated games; 48 full-strength games excluded as uncalibrated. These nominal engine anchors are not human ratings, and the interval excludes systematic anchor calibration error.

The first-20 no-mate target and castling target were met (castled on move 5). Whole-queen retention failed on moves 18–19. The full game was lost. Zero illegal moves did not imply a correct guard model or safe king.

Own observations, no engine analysis:
- 16...Nxe4 took a knight whose pawn guard could have recaptured, but White instead played Qb3. I then missed the checking fork 18.Bxe6+: the bishop checked my king on g8 and attacked my queen on d7, with White's queen on b3 guarding e6. My 18...Qxe6 / 19.Qxe6+ lost queen 9 for bishop 3. The earlier knight gain and e6 pawn loss left a nominal deficit of four.
- 28...Be5 left that bishop guarded only by the f7 knight. After 30.Rc5 attacked it, 30...Nh6 removed its guard. I tracked the separate g5 pawn guard but overlooked the bishop. 32.Rxe5 then captured the whole bishop.
- 34...Nxe2+ / 35.Rxe2 traded my knight 3 for White's rook 5, recovering two. This was not a whole-rook loss by me.
- 43...bxa4 gained a pawn when White declined to recapture. My resulting passed pawn reached a3, but had not promoted when the game ended. 45.hxg5+ Kxg5 was a fair pawn pair. Final nominal material deficit was three: Black two rooks, one knight, four pawns versus White queen, rook, bishop, three pawns.
- After 49...Kh6 50.Re5 my king had no immediate legal flight: g5/h5 were controlled by Re5 (h5 also by White's g4 pawn), g6/h7 by Qc2, and g7 was occupied by my pawn. I identified the Rh5 threat, but failed to check the other rook check. 50...g5 blocked Re5–h5 while putting my own pawn on g5. Actual 51.Re6# checked along e6–f6–g6–h6. g6 was controlled by the rook and queen; h7 by Qc2; g7 by Bc3 once Re5 departed; h5 by White's g4 pawn; g5 was my own pawn. Neither rook, the b2 knight nor a pawn could capture the checker or interpose on f6/g6. This was an actual referee mate, not a proved forced earlier line.

Decision: a single-threat defense is insufficient. Before committing to a pawn blocker beside my king, inspect the opponent's other immediate checks and rebuild the king's flights after the source square is vacated. The earlier 49...Kf7 is my unplayed repair hypothesis. I do not claim that it saves the game. Likewise 17...Kh8 instead of Nd6 is only an untested hypothesis about the earlier bishop fork, not evidence of transfer.

Timing: analysis repeatedly grew into long remote variations and updates were too far apart. This remained unrepaired. There is no measured per-move token counter, no fixed inference budget, and no efficiency claim.

## Predeclared trial 239
Recorded practice, maximum-strength opponent, Black, game 142 after ply 97 (49.Qc2+), four own moves maximum. Choose 49...Kf7 by my reasoning, then respond to actual replies. Targets: no mate during the four-move drill; no whole queen/rook loss; nominal final deficit at most four (initial deficit three). Stop explicitly after four own moves if still active. A stopped drill, especially with an unanswered final opponent move, does not prove an ending saved. Record the actual outcome and decision before benchmarking again. Next formal fixed-rotation evaluation remains 144 scored games.

## Trial239 / practice121 outcome

Maximum-strength opponent, Black from142 ply97. Actual line: 49...Kf7 50.Qf5+ Kg8 51.Qe6+ Kf8 52.Qe7+ Kg8 53.Qxg7#. LOSS after four own moves / eight plies, zero illegal. Referee seq1213, timestamp2026-10-09T05:24:02.101552+00:00. The normal referee PGN request remained queued for admission; I read only my small completed saved file data/practice/games/000121.pgn.gz with gzip, as for completed benchmark PGNs. No engine output or analysis was consulted. The queued read request has not changed a game.

No-mate target FAILED. No-whole-queen/rook target MET. Final nominal deficit at most four MET exactly: initial three, then g7 pawn lost. Qg7 was guarded by Bc3 through d4/e5/f6. King g8 could not capture that guarded checker. Qg7 controlled f8/f7/h7, my rook occupied h8, and no other unit could capture or interpose against the adjacent g7–g8 check. The earlier retreat hypothesis did not save even this four-move drill. I do not claim that every alternative at move49 loses by force. My unplayed Kh7 at move51 has a possible Rh2 mating response in my mental calculation; this is not an independently established forced line.

Decision: the late king-flight trials have not transferred a safety repair. Return to an earlier concrete material-and-check error before benchmarking143. A long checklist and zero illegal moves are not evidence of learning.

## Predeclared Trial240

Recorded maximum-strength practice, Black, benchmark142 after ply33 (17.Qb3), four own moves. Own hypothesis: 17...Kh8 moves the king off the e6–f7–g8 bishop-check diagonal before Bxe6. It deliberately gives up the immediate checking fork's tempo; a subsequent d3xe4 may recover White's lost knight, which must be counted honestly. Targets: no mate over four own moves; no whole queen/rook loss; final nominal deficit at most one (initial Black nominal advantage three). Respond only to actual opponent moves. Stop explicitly after four own moves if still active; preserve unanswered final replies. No full-game-save or benchmark-transfer claim from a local drill. Next benchmark143 / next formal144.

Considered and rejected before play: 17...Nc6-d4 would guard e6 and attack Qb3, but White's e3 pawn can capture that knight cheaply. It was not played or counted as practice.

Practice121 diagnosis clarification: Qg7 also attacks h8 diagonally, in addition to f8/f7/h7. My rook occupied h8, but vacating that body alone would not make h8 a legal flight in the actual final position. Do not attribute this mate solely to the rook body.

Trial240 outcome, 2026-10-09: pending session48065 admitted at 17:06:39 UTC and started practice122, maximum-strength Black from benchmark142 ply33. Own moves Kh8, Nd8, Bd6, Qe8; actual White replies dxe4, Bb2, Bg4, f4. Stopped after four own/eight total plies, zero illegal attempts, result * (no score). No mate or whole queen/rook loss; final nominal material equal, so all predeclared local targets met. White f4 pressure against e5/g5 remains unanswered: not a saved-game claim. Decision: test king safety and guard preservation in fresh benchmarks143-144 (Trial241), formal evaluation after144. Observe early whole-major losses/checking forks and final king safety alongside benchmark outcomes; no causal improvement inferred from this remembered drill.
