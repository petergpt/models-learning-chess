# Benchmark162, formal review, trials269–270

162 Black nominal1800: loss by31Bb2#,61plies,1illegal submission25Rd4e3 (rook diagonal). Resultseq12945,2026-10-10T00:14:26.904355+00:00. Own PGN data/games/000162.pgn.gz read to verify finish; no chess-analysis code or outside advice.

Played e5 Nf6 d5 d4 Nxd5 Qxd5, en-passant dxc3 against c4 queen attack, Qxd1+; developedNc6 Bc5 O-O Bd6 Be6. Extra pawn and reasonable center after bishop/knight exchanges. Rad8 d4 Bxc6 bxc6 Bd2 e4 fxe4 fxe4 Rxf8+ Kxf8 cxd4 Rxd4 Rc1 Bd5 Be3. Illegal diagonal rook capture rejected; correctedRd3. Kf2 Ke7 b5 Kd6 Ke2 Ra3 Bc5+ Ke5 Bxa3 Kd4 Bb2#.

Decisive failure28Ra3: WhiteBc5+ forked Kingd6 and rook a3 along c5-b4-a3. b4 had vacated earlier. I focused on the king check and failed to see the rook attack. AfterBxa3,30Kd4 walked into31Bb2#: bishopb2-c3-d4 checks and covers e5; Rc1 covers c4/c5; Ke2 covers d3/e3; ownBd5 andPe4 occupy d5/e4. All king exits unavailable. No forced-loss proof was used before finalmove; referee recorded checkmate. One illegal move, rook loss and missed mate contradict a claim that current safety method is fixed.

Formal cycle157–162:3W0D3L (two maximum losses, two skill0wins, one1800win/one1800loss). At15643W8D105L Elo1540[1410,1660]; at16246W8D108L Elo1580[1460,1710]. Fullstrength0/0/54; skill0 38/4/12; nominal1800 8/4/42. Conditional95% Bayesian credible interval,latest50ratedof108;54maximumexcludeduncalibrated. Nominalanchors/model; not FIDE/platform, systematic calibrationerror excluded. Estimate increased even after162loss because rolling50 composition changes; not evidence this loss improved play. Broad overlapping intervals and repeated major errors mean no sustained method improvement established. Positive161conversion and159pawnfork coexist with opponent gifts and162failure.

## Trial269 / practice142

Weakness: missed forcing bishopfork and ensuing mate; king as rook defender can be displaced by checks. From162ply55 beforeRa3, maxBlack: Ke5 bxc6 Be6 Bxa7 Rd6 Bb8. Threeown/sixplies0illegal; stoppedunfinishedseq1399 at2026-10-10T00:19:03.492555+00:00. Two pawns lost; rook still on board but Bb8 pins/attacksRd6 againstKe5. Bxd6+ Kxd6 appears to win exchange. Remembered short repair failed to establish safety, equality, or transfer.

## Trial270 / practice143

Custom FEN from own practice142 afterBxa7: 8/B5pp/2P1b3/4k3/P3p3/3r4/4K1PP/2R5 b - - 0 30. MaxBlack. TryKd5 insteadRd6. Kd5 Rc5+ Kd4 c7 Rc3 Rc6+. Initiallytwoownmoves, extendedtothree to contest promotion support. Sixplies0illegal; stoppedunfinishedINCHECKseq1408 at2026-10-10T00:20:54.495619+00:00. Rc6+ uncovers bishop a7-b6-c5-d4 check. My anticipated Rxc6 would not resolve it; king defense ofRc3 is disrupted. Repair unproved/likely loses material, not a successful trial. No practice score, no Elo contribution.

## Decision / trial271

Return to benchmark163, nextformalreview168. Change emphasis from static defender counts to identifying the actual checking piece and all lines uncovered by a forcing move, particularly when the king guards another piece. Before committing to a rook manoeuvre, mentally trace opponent bishop checks through squares vacated by pawns and through the rook destination. Keep actual piece geometry and own blockers explicit. Observable transfer163–168: avoid bishop check-forks/discovered checks that remove a rook's defender, and avoid illegal piece geometry. This procedural change is a hypothesis, not learning evidence; do not claim a longer checklist establishes progress. Short remembered drills have repeatedly failed to settle safety.

## Boundary incident

After162, ./play export unexpectedly returned a path under /home/peter/Chess Learning/deliverables/ with another model label in the filename. Only the tool's printed path was seen. Did not open/read the artifact, inspect shared deliverables, publish, alter website, or import other learner material. Avoid further export commands; benchmark/play/status/practice remain functional. No manual changes to operator files/data. File-name enumeration was restricted to own data directory and own162PGN; no sibling/operator-central material read.
