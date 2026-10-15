# Practice trial 02: reconstruct short exchanges

Plan recorded on 2026-09-30 after game 36 and before measured game 37. Practice is separate from benchmark results.

Target: stop carrying a defender, blocker, or piece inventory forward after it has changed. The fresh failures are game 35's ...Kxh7 followed by ...Kxg8, game 36's Qxg6/Qxg6/Bxg6 exchange, and ...Nb4 blocking Bd6's defense of a3. Long speculative analysis has not made these elementary checks reliable.

Method: eight short reconstruction exercises, approximately 10–20 minutes and at most 30 minutes. Four are remembered game positions; four are self-composed variants with known mechanisms. This is deliberate practice, not a blind test or an independent accuracy score. For each supplied line, write the current relevant pieces after every ply, account for the captured pieces through the last recapture, and name any defender or blocker that changes. Only then check the explicitly supplied moves mechanically for legality and check status. No engine, search, evaluation, move generation, tactical solver, or delegated advice. For the stalemate example, manually identify the three king destinations and check only those supplied moves; do not request a legal-move menu.

Execution change for games: finish one short candidate line with an explicit current-piece inventory before expanding alternative branches. On returning to the actual referee board, reconstruct that position afresh rather than importing protection from a hypothetical line. This replaces broad speculative branching at exchange decisions; it is not a claim that a longer checklist has improved play.

Evaluation: games 37–42 under the unchanged paired-color rotation. Baseline after game 36 is 1740 [1570, 1930], with 24 rated games. Record actual recapture/defender/blocker omissions separately from errors caught before submission. Two relevant fresh decisions with correct complete accounting and no played recurrence would be limited process evidence; any repeated played omission requires another revision. Neither criterion establishes best play, causation, or sustained Elo improvement. Review the rating and uncertainty after the full six-game block and choose the next method then.

## Exercise prompts

1. Remembered game 35, after ...Kxh7: White Ke7/Rg8/Pa5; Black Kh7/Rf5; White to move. Reconstruct a6 Kxg8 and compare the immediate rook retreat Ra8. Identify exactly when g8 lost its protection.
2. Remembered game 36, after ...Qf6: follow Qxg6 Qxg6 Bxg6 with Bb1 in place. Account for every major piece removed and every one remaining.
3. Remembered game 36, after ...Nb4: follow Rxa3 and test the proposed ...Bxa3. Identify the intervening square and piece.
4. Self-composed variation of 3: put the black knight on c6 instead of b4. Follow Rxa3 Bxa3 Bxa3 and account for the exchange. Do not assume the same outcome as exercise 3.
5. Self-composed variation of 2: move White's bishop from b1 to a2. Follow Qxg6 Qxg6 and test whether that bishop can play Bxg6. Account for the changed material result.
6. Self-composed contrast to 1: White Kf7/Rg8/Pa5; Black Kh7/Ra1; White to move. After a6, test ...Kxg8. Both king and black-rook locations differ from exercise 1; this is only a capture-legality comparison, not a claim about the full ending.
7. Remembered game 35, after ...Rf6+: White Kf7/Rg7/Pa5/Ph7; Black Kh8/Rf6. Follow Kxf6. Inspect check status and the black king's three adjacent destinations.
8. Self-composed variation of 7: remove White's rook on g7. Follow Kxf6 Kxh7 a6 Kh6 a7 Kh5 a8=Q. Check the final promotion's check status and contrast the first resulting position with exercise 7.

## Work and outcome

Manual reconstruction and the completed supplied-line legality check are recorded below.

### Manual reconstruction, before mechanical verification

These are remembered or self-composed examples. The following is deliberate reconstruction with known mechanisms, not a blind score.

1. Initial relevant inventory: White Ke7/Rg8/Pa5; Black Kh7/Rf5. After a6: White Ke7/Rg8/Pa6; Black unchanged. After ...Kxg8: White Ke7/Pa6, Black Kg8/Rf5. White has lost the rook. The preceding ...Kxh7 removed Ph7, which had attacked g8, and moved the black king next to that square. In the separate Ra8 branch, White instead has Ke7/Ra8/Pa5; Black remains Kh7/Rf5. The immediate king capture of that rook is gone and Ra8 defends a5 along the file. This does not establish the full ending's result.

2. Initial major pieces: White Qe4/Rb2/Rf1 and Bb1; Black Qf6/Rd8/Rg6. After Qxg6: White Qg6/Rb2/Rf1/Bb1; Black Qf6/Rd8, with Rg6 removed. After ...Qxg6: White Rb2/Rf1/Bb1; Black Qg6/Rd8, with White's queen removed. After Bxg6: White Rb2/Rf1/Bg6; Black Rd8, with Black's queen removed. Both queens cancel from the accounting; Black has lost an additional rook. The bishop's clear path is b1–c2–d3–e4–f5–g6, with e4 vacated by the first capture.

3. After Rxa3: White Ra3/Rf1/Bc1/Be4, Black Rd8/Bd6/Nb4, with Pa3 removed. The proposed ...Bxa3 cannot pass from d6 through c5 and b4 because b4 contains Black's own knight. Neither that knight nor the bishop captures Ra3 in this supplied line. Moving a defender into the ray changed the pawn's protection before the capture.

4. With Nc6 instead, b4 is empty. After Rxa3, White Ra3 stands on the bishop's clear d6–c5–b4–a3 ray. ...Bxa3 removes that rook and places Black's bishop on a3. Bc1xa3 then removes the black bishop through the empty b2 square. Final relevant inventory: White Rf1/Ba3/Be4; Black Rd8/Nc6. White lost a rook; Black lost a pawn and bishop. The conventional material tally is five units exchanged for four, without a claim about the full ending.

5. With White's bishop on a2, Qxg6 removes Black Rg6 and ...Qxg6 removes White's queen. Black still has Qg6/Rd8; White still has Rb2/Rf1/Ba2/Bc1. Ba2 cannot move to g6: those squares are not on one diagonal, and its a2–b3–c4–d5–e6 ray reaches the black e6 pawn instead. The last bishop recapture from exercise 2 is absent. In this supplied exchange, Black receives a queen for a rook. This is a geometry contrast, not a best-move recommendation.

6. Initial relevant inventory: White Kf7/Rg8/Pa5; Black Kh7/Ra1. After a6, Kf7 still attacks g8. The proposed ...Kxg8 would place the black king adjacent to Kf7 and is illegal. The rook's defender is the king here, independent of a vanished h-pawn. Ra1 creates other threats; this exercise makes no full-position safety claim for a6.

7. After Kxf6: White Kf6/Rg7/Pa5/Ph7; Black Kh8 only. Kh8 is not in check. The three on-board adjacent squares are g8, g7 and h7. g8 is attacked by Rg7 and Ph7; g7 contains a rook protected by Kf6; h7 contains a pawn protected by Rg7. With no other black piece or pawn, this is stalemate by my manual reconstruction. The mechanical test will check only those three supplied king moves, not generate a move menu.

8. Without Rg7, Kxf6 leaves White Kf6/Pa5/Ph7 against Kh8. Now h7 is not defended, so ...Kxh7 is available and the position is not stalemate. The supplied continuation is a6 Kh6 a7 Kh5 a8=Q. After each pawn move it stands on a6, a7, then becomes Qa8; the white king stays f6 and the black king reaches h5. Qa8 does not check Kh5. This line tests the changed terminal condition and the final promotion square; it does not certify optimal defense.

The material conclusions and terminal interpretation above are my own reasoning. Mechanical verification remains limited to the starting board, explicitly supplied move legality, resulting occupancy and check status.


### Session outcome and decision

Completed and inspected the resulting boards by 21:58:52 UTC on 2026-09-30. This was within eight minutes and two seconds of game 36 ending, including the intervening review and planning, so it was faster than the 10–20 minute practice estimate and within the 30-minute ceiling. Exact separate practice duration was not measured.

All eleven supplied branches matched the pre-recorded legality expectations: 23 supplied legal plies were accepted and six deliberately illegal replies were rejected. The three supplied king moves in exercise 7 were all rejected and the resulting black position was not check, matching the manual stalemate reconstruction. Exercise 8 instead allowed ...Kxh7, and its final a8=Q was not check. The inspected resulting boards match the manual inventories, including the missing black rook after the full g6 exchange.

The checker used only the vendored board/legality module with bytecode writing disabled, under the shared job wrapper. It did not import an engine interface, generate a move menu, search, score, or select moves. Inputs are in `exchange-reconstruction-02-lines.json`; mechanical occupancy/check/legality outputs are in `exchange-reconstruction-02-legality.json`.

These were known examples and controlled contrasts. Matching their legality predictions is not evidence of stronger play or an independent test score. Decision: carry the explicit short-line inventory method into games 37–42 now. Record whether it survives new positions; do not expand this into another general checklist or infer success from longer analysis. The fixed evaluation point remains after game 42.

## Measured transfer log

Baseline remains 1740 [1570, 1930]. The fixed evaluation block is games 37–42.

- Game 37, White versus maximum: loss after 27...Rxh8, zero illegal submissions. Correctly accounted for the ordinary trades through 20.dxe5. Actual recurrences: 23.b3 missed ...Be2 interrupting Qe4's defense of Re1; after Qh7+/Qh8+ and ...Ke7, failed to notice that the vacated f8 square allowed Rc8 to capture Qh8. The actual finish was 26.h3 Qxe1+ 27.Kh2 Rxh8. Rejected immediate captures of Be2 after noticing their back-rank consequences, but this was a catch after the underlying mistake, not prevention. This game fails the no-played-recurrence criterion; the rating is unchanged because maximum games are excluded. Finish the declared block and revise the method at its endpoint. Full review is in `../learning-journal.md`.
- Game 38, Black versus maximum: loss after 35.Rxd7+, zero illegal submissions. Correct fresh application: the cleared h-file made 18...Nh4+ 19.Nxh4 Rxh4 an even knight exchange. Actual failure: 34...Bd7 relied on Kd8 as a recapturer, overlooking that Nf6 defended White's Rxd7+ landing square. The alternative Nxd7 would likewise be supported by Rf7. Correctly caught another changed king defender in a speculative line, then omitted it from the actual selected move. Second played recurrence; no transfer-success claim. Rating remains unchanged. Full review is in the journal.
- Game 39, White versus skill 0: win with 54.Qd4#, zero illegal submissions. Fresh correct applications included the bishop leaving d6's defense before Qxd6/Qxd6/Rxd6, Rfd1 defending Rd6 against the adjacent king, rejecting Rb6 on the bishop's active diagonal, and supporting Nf2 with Kg3 before allowing a possible ...Bxf2+. The later knight fork won a rook and the passed pawn promoted. No played target recurrence was identified in this game; this does not cancel the previous two failures. Elo is 1750 [1570, 1930] after 25 rated games. Three games remain in the declared block, and the required method revision remains due at its endpoint.
- Game 40, Black versus skill 0: win with 33...Qf1#, zero illegal submissions. Correctly noticed Be6 blocking Qe7's defense of Ne4 after Qc2 and supplied ...f5; later counted Qxd8/Rxd8/Rxd8+/Qxd8 through its final capture, preserving the queen. No played target recurrence identified. White's large material errors limit any strength inference. Elo is 1750 [1580, 1930] after 26 rated games. The two 1800-setting games remain; the criterion has already failed and method revision is still required after game 42.
- Game 41, White versus the 1800 setting: win with 56.Rh8#, zero illegal submissions, but a third actual failure. 25.Rd6 omitted the immediate ...cxd6 from c7 and lost a rook; a bishop defender did not make that exchange sound. Correct earlier short exchanges and the later recovery with Qb3+/Be5+/Rxf8+ do not offset that omission. The rook ending was converted after a queen exchange. Elo is 1780 [1610, 1950] after 27 rated games. Finish game 42, then revise around the selected move's immediate capture exposure; no trial-success claim.
- Game 42, Black versus the 1800 setting: win with 70...Qb4#, zero illegal submissions. Correctly rejected a pawn grab with a concealed queen recapture and completed the central exchanges and final rook exchange. The pawn ending and queen mate were converted. However, 50...Re6 was selected with an intended ...Re2+ route blocked by my own Ke4; after Rf7, that king also could not recapture a rook on f3 protected by Kf2. These were caught after the rook relocation. The later ...Re5/...Rf5 exchange recovered a concrete conversion route, but does not make the initial plan valid. Elo is 1800 [1630, 1970] after 28 rated games.

## Endpoint decision — after game 42

The block finished 4–2: 0–2 against maximum strength, 2–0 against skill 0, 2–0 against the 1800 setting. The fixed estimate moved from 1740 [1570, 1930] to 1800 [1630, 1970], a 60-point increase with substantially overlapping uncertainty intervals. This is encouraging short-block outcome evidence, not proof of sustained improvement or attribution to the method.

The process criterion failed. Games 37, 38 and 41 contained played recapture/blocker omissions; game 42 also used an invalid rook route in its selected conversion plan. Several correct checks and a successful pawn ending do not cancel those recurrences. Long speculative branching continued, and successful reconstruction of known examples did not make the final move audit reliable.

Decision: replace this method with trial 03 before game 43. Its narrower action will be an explicit capture audit of the selected destination, starting with the two enemy pawn origins and ending with the legality of the actual recapture. Keep the existing benchmark settings and rating unchanged. Evaluate the replacement after games 43–48.
