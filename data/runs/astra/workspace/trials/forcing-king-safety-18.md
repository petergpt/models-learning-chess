# Trial 18 — forcing king safety and recapture contrasts

Declared 2026-10-02 22:07 UTC after game 132, with no active game. Baseline: 1580 [1460,1700], 51W/3D/78L in 132 scored games; MAX 0W/2D/42L, skill 0 38W/1D/5L, nominal 1800 13W/0D/31L (44 each). The user endpoint is exactly 200 scored games. This trial's fixed benchmark block is 133–138 in the unchanged paired-color rotation.

## Weakness and method

Trial 17 did not transfer reliably: the material calculation repeatedly stopped before a forcing check or treated a nearby king as a recapturer without retaining the opponent's surviving defender. Revisit this already-failed skill explicitly; this is not a novel checklist or a claim that recalling a diagram is improvement.

First make and mechanically check eight manually specified contrast cases from our own games 128, 130 and 132. Only board reconstruction and legality of the specified moves are allowed. No generated move menu, attack-map analysis, search, engine evaluation or external source. The remembered positions are training examples, not held-out tests.

Then play exactly two fresh self-composed opponent-practice positions at nominal 1800, White then Black, at most 20 own moves plus the reply in each. Unlike trial 17's sparse rook drills, both positions retain queens, rook, bishop, knight and six pawns per side, including constrained castled kings and diagonals that can open when blockers move. These are equal-material constructions, not certified equal evaluations.

Combined study/practice deadline: 2026-10-02 22:52:05 UTC, 45 minutes from the post-132 review clock. End any ongoing practice at its move cap or this deadline; record early results or unfinished sessions and add no replacement practice. Return to benchmarks after both sessions, even if the exercises fail.

Position A, White:
5rk1/p1pq1ppp/1b2p3/3n4/3N4/1B2P3/P1PQ1PPP/5RK1 w - - 0 1

Position B, Black:
6rk/pp2qppp/3bpn2/8/8/3BPN2/PP2QPPP/6RK b - - 0 1

## Predictions written before legality checks

1. Game 132 after ply 104 (...Bb6): Nxb6/Kxb6 is legal because the knight leaves c4 and Rd1 does not guard b6.
2. From that same position, Rd6+/Kc5/Rxb6 is legal, but Kxb6 is illegal: Nc4 survives and protects b6.
3. From that same position, Rd6+/Kc5/Nxb6 is legal, but Kxb6 is illegal: Rd6 now protects b6.
4. Immediately after Rd6+, Kxd6 is illegal because Nc4 protects d6.
5. Game 130 after ply 61 (Rc8+): Kh7 is illegal because h7 is occupied; Kf8 is illegal because the checking rook controls f8. Re8/Rxe8 are legal and the recorded result is mate.
6. Counterfactual to case 5 with only the black h7 pawn placed on h6: Kh7 is legal. This demonstrates an actual escape square, not a certified best earlier plan.
7. Game 128 after ply 35 (Qg8+): Kxg8 is illegal while Bb3 protects g8. Nxg8/Nf7 are legal; the recorded result is mate, so winning the queen did not make the capture safe.
8. Counterfactual to case 7 with Bb3 removed: Kxg8 is legal. This deliberately changes material and is only a geometry contrast.

## Evaluation and decision

The practice target is to preserve a usable king response through checking continuations and to reject false king recaptures in the actual final board. Track actual mating losses, newly opened pins, unsupported material losses and illegal submissions; retain all other errors as well. Success on remembered cases is diagnosis/retention only. Fresh practice is still training, not Elo evidence.

Use ordinary development in games. A short cue replaces trial 17's special rook focus: when a capture gives or permits check, resolve the king response before counting the gain; a king recapture must be legal with every surviving enemy defender still present. Do not expand the cue into an exhaustive move checklist or assume a king-adjacent piece is secure.

At game 138 report the whole block's W/D/L, per-opponent results, Elo and uncertainty, along with recurrence of the targeted errors. A recurrence rejects reliable execution and requires another revision. No single win, clean drill or transient rating rise establishes sustained progress. No opponent, estimator, decision-time target or token counter is changed.


## Contrast study completed — before opponent practice

Eight predeclared case groups were checked as eleven supplied branches, 21 specified plies: 15 legal continuations and six deliberately illegal king moves. Every starting board was valid and all predictions matched. Inputs, the supplied-move-only verifier, and results are saved in king-safety-18-inputs.json, king-safety-18-verify.py and king-safety-18-legality.json.

The check used only the existing vendored board module, with bytecode writes disabled and the shared t3-job wrapper. It reconstructed our recorded SAN moves and checked the explicitly supplied UCI moves. No engine interface, search, generated move menu, attack map or evaluation was used. The two mating outcomes are from the recorded referee results, not a new automated evaluation.

The 132 contrasts distinguish Nxb6 before Rd6 (king recapture legal), Rxb6 after Rd6 (Nc4 survives), and Nxb6 after Rd6 (Rd6 survives). Both later king recaptures are illegal. The 130 counterfactual makes h7 available only by actually vacating h7; merely naming it did not create an escape. The 128 contrast confirms Bb3's role in preventing Kxg8, while the recorded Nxg8/Nf7 sequence shows that a legal queen capture can still allow mate.

These were known failures with written predictions, so passing them is diagnosis/retention only. Proceed to the two declared fresh positions without extra examples or changed limits.


## Practice 31 — fresh White position A

Stopped at the declared cap on 2026-10-02 22:27:15 UTC: 20 own moves / 40 plies, zero illegal submissions, unfinished rather than a win or draw. Result seq 984, sha256 5654baa3c792f9e85a54a85bce6174723c175e7cc1858ad2bc0652ff8c982b70. PGN read back.

1.h3 Nf6 2.Rd1 c5 3.Nf3 Qb5 4.c4 Qc6 5.Qc2 Rb8 6.Nd2 Qc7 7.e4 Nd7 8.Nf3 Ne5 9.Nxe5 Qxe5 10.Rd7 Bc7 11.g3 Ba5 12.Kh2 h5 13.f4 Qf6 14.e5 Qh6 15.h4 g6 16.Rxa7 Bb6 17.Ra6 Qf8 18.a3 Qe8 19.Ba4 Qd8 20.Bb5 Ra8.

h3 created an initial h2 escape. Rd1 supplied a real queen defender before Nf3 opened the d-file; c4 stopped a pawn advance that would restrict Bb3 behind a2/c2. Nd2 added e4 support before the pawn advanced. After Qc7 and later Qxe5, I explicitly stopped treating h2 as safe. Bc7 created the queen-bishop battery; g3 blocked it with f2 support, and Kh2 was chosen only after checking the actual diagonal. f4/e5 gained queen tempi with pawn support, and h4 closed the pawn contact.

The knight exchange completed at equality. Rxa7 won the pawn only after its bishop defender left b6, and the planned Ra6 retreat was actually used after ...Bb6. I kept a4 clear by a3 rather than a4. Ba4 forced the queen off e8, then Bb5 restored the rook exit and put the bishop on a c4-supported square protecting Ra6.

Final board: White Kh2/Qc2/Ra6/Bb5/a3,c4,e5,f4,g3,h4 versus Black Kg8/Qd8/Ra8/Bb6/c5,e6,f7,g6,h5. White has one extra pawn. No unexpected material loss, mating loss or illegal move occurred within the cap. Black's final ...Ra8 attacks Ra6. The bishop-support geometry was planned, but no further rook exchange or recapture was played; do not report a completed defense, conversion or practice win. This is positive training execution, not measured Elo evidence.

## Trial 18 practice B and training endpoint — 2026-10-02 22:43 UTC

Practice 32, Black, nominal 1800, fresh self-composed FEN `6rk/pp2qppp/3bpn2/8/8/3BPN2/PP2QPPP/6RK b - - 0 1`, ended exactly at the declared 20 own moves plus final opponent reply (40 plies). Referee result is unfinished, not a win/draw/loss; zero illegal submissions. Result seq 1027, hash `1cfdca0761e4e96e4333a5db074df29aee2173b957c74864f9691116bd4afdef`, timestamp 22:43:06. PGN read back in full.

Actual moves:
1...Rf8 2.a3 e5 3.Bb1 e4 4.Nd4 Qe5 5.f4 exf3 6.Nxf3 Qh5 7.g3 Re8 8.b4 Ne4 9.Bxe4 Rxe4 10.Kg2 f5 11.Qd3 Be7 12.Rc1 h6 13.Kf2 g5 14.Qd7 g4 15.Rc8+ Kh7 16.Nh4 Qf7 17.Nxf5 Re5 18.Rc5 Rxc5 19.bxc5 Qa2+ 20.Kg1 Qb1+ 21.Kf2.

Observed useful execution:
- Rf8 opened g8 while Qe7 guarded f8; no assumed king recapture from h8 to f8.
- e4 blocked Bb1-h7. The actual f4/exf3 en-passant/Nxf3 sequence exchanged pawns and changed the queen attack and h2 defense; no pawn win was claimed.
- Bxe4/Rxe4 was an actual equal minor exchange. White Kg2 ended the earlier h-pawn pin.
- Once White Rc1 made Rc8+ concrete, h6 created h7. White's bishop had gone; later Qd7 was blocked by Be7. The actual Rc8+/Kh7 response was legal.
- Recognized the bishop pin on the seventh rank and inserted Qf7 as a second blocker.

Errors and limits retained:
- The claims that f5 was defended were materially incomplete. White Qd7 and Nh4 jointly attacked it, and 17.Nxf5 won the pawn. Qxf5+ would allow Qd7xf5+, so queen protection was not an adequate recapture. This repeats the effective-defender weakness.
- Rxc5/bxc5 was an equal rook trade. An immediate Bxc5 would open Qd7's attack on Qf7. Qa2+ moved the queen with check, but my initial planned bishop recovery still failed: Be7 was again the sole blocker between Qd7 and Kh7, so Bxc5 would be illegal. This was recognized before submission. The final Qb1+ bought another king response but did not solve the bishop problem.
- Final Black Kh7/Qb1/Be7 with a7,b7,g4,h6 versus White Kf2/Qd7/Nf5 with a3,c5,e3,g3,h2. One pawn down, bishop pinned and attacked, no resolved defense or conversion. No illegal move was submitted.

Both declared practices are now complete, both unfinished at 20 own moves and zero illegal attempts, before the shared 22:52:05 deadline. Practice A ended one pawn up with a final rook attack still unresolved; B ended one pawn down with an unresolved bishop pin. Eight remembered contrast groups passed their specified legality predictions, but that is retention, not transfer. Fresh B already reproduced an inadequate recapture assumption, so these drills do not establish reliable king-safety execution or improved playing strength.

No extra practice or selective extension. Proceed with the predeclared unchanged fixed benchmark block 133–138, assessing all six results at 138. Baseline remains 1580 [1460,1700], 51W/3D/78L after 132; training is excluded from ratings. The run stops at 200 scored benchmarks regardless of Elo. No valid new cumulative token counter is available. The tool goal still contains the obsolete win-based objective and old blocked status; the explicit user endpoint and current AGENTS/GOAL govern this continuation.

## Benchmark 133 — White versus maximum strength — loss, 2026-10-02 23:00 UTC

41 own moves, 82 plies, zero illegal submissions. Practical resignation after 41...Kxa4 with N+2P versus N+5P and connected Black a/b passers; legal continuations remained, not checkmate or a proved forced win. Result seq 11016, hash `90194b603881f7e1a8f6924809e1f44a584d2ae27bfdd10e5d759ae196517515`; snapshot `a84f8d5f14e518687af2594d20dc7cba511e8549ba6c9f5ab5038e365973a7cb`. Full PGN read back.

Normal development: castled move6, all minors developed move8, first rook move11 and second13, first15 moves without material loss. h3 created a currently legal h2 escape; no later back-rank mate occurred. c4/dxc4/Nxc4 exchanged central pawns, leaving isolated d4. Nce5 deliberately retained Nf3 as a d4 defender.

Error: 18.Bd3 was annotated as retaining Qd1 and Nf3 on d4, but Bd3 itself blocked the queen line. This was noticed at 19.Qxc1 after ...Rxc1, not before the bishop move. ...Bxd3/Nxd3 and ...Nf5 left d4 under three-piece pressure. Qf4 did not restore a sufficient defense; ...Nxd4/Nxd4/Qxd4/Qxd4/Rxd4 cost the pawn while otherwise exchanging material equally. This is another blocked/effective-defender failure, not a new mating failure.

The rook sequence Ne5/Re4/Nf3/Rxe1+/Nxe1 was handled with an actual knight recapture; Kg1 could not recapture e1. Endgame: a4 avoided an undefended-a2 fork, and after Kf3/f5, Nb2 was played before the actual ...e4+, avoiding a check-and-knight fork. Kxe4 was correctly rejected because f5 guarded it. Nd3+ later was rejected because e4 could capture the checking knight. These are local observed/identified tactics, not evidence that the ending was held.

Black's checks drove the king backward, then Kc5–b4–xb3 and ...Kxa4 took both queenside pawns. f3/exf3/gxf3 exchanged the central pawn, and h4 saved h3 from the knight attack, but no adequate defense of the queenside was found. Final: White Kd2/Ne3/f3,h4; Black Ka4/Nf4/a5,b6,f5,g6,h6.

Cumulative 51W/3D/79L from133; MAX 0W/2D/43L from45. MAX remains excluded from the nominal rating, so the displayed baseline estimate remains1580 [1460,1700]. Trial18 block133–138 continues as declared; one loss alone is not its full endpoint assessment. No additional practice inserted.

## Benchmark 134 — Black versus maximum strength — loss, 2026-10-02 23:14 UTC

27 own moves, 55 plies, zero illegal submissions. Practical resignation after 28.Qxd5, a bishop and two pawns down with the central counterplay gone; legal defensive continuations remained, not a mate or proved forced loss. Result seq11073, hash `f2983dc23209582c25bedb212b9f7dee26aaf292af5eec514481bfd6fbc06b36`, snapshot `d1ea746beb9902d73a338d175a7ec6e20cb6aa5fd1fc019f82e0ec42f00f662a`. Full PGN read back.

Ruy Lopez development: castled7, all minors developed9. Bb7 cleared c8 so the queen could recapture on a8 if the a-file opened. Na5/c5/c4 gained space; Nd7/f5 attempted a central break. No claim that the resulting position was objectively good.

Decisive failure: after 15.exf5 I recognized that the promised Rxf5 was unsound because White's e-pawn departure had opened Bc2-d3-e4-f5. But the replacement 15...Bxd5 overlooked Qd1-d2-d3-d4-d5. Actual 16.Qxd5+ won the undefended bishop and checked along the newly open d5-e6-f7-g8 diagonal. Kh8 was a legal reply. Catching the first bad candidate did not make the replacement sound.

Nf6 chased the queen, axb5 restored pawn parity, and the actual Rxa8/Qxa8 exchange was correctly recaptured. Another effective-defender error followed: d5 removed the d6 pawn's defense of e5. Nc6 alone did not hold it against Nf3 and Re1; Nxe5/Nxe5/Rxe5 cost another pawn. Bd6/Re6/Qc6/Bf4 created a relative pin of Bd6 to Qc6. Ne8 added a rook-supported defender, and the actual Bxd6/Nxd6 exchanged bishops without a further piece loss. Qd7 moved out of that alignment but White Qxd5 took the remaining center pawn and supported Re6.

Final Black Kh8/Qd7/Rf8/Nd6/b5,c4,g7,h7 versus White Kg1/Qd5/Re6/Bc2/Nf3/b2,c3,f2,f5,g2,h3. No material recovery or reliable forcing-safety transfer established.

Cumulative51W/3D/80L from134; MAX0W/2D/44L from46. The nominal rating remains1580 [1460,1700] because MAX is excluded. Trial18 is0W/0D/2L so far, with its complete assessment still fixed at138. Continue135–138 in unchanged rotation, without extra practice.

## Benchmark 135 — White versus skill0 — checkmated, 2026-10-02 23:34 UTC

37 own moves, 74 plies, zero illegal submissions; actual 37...R8e3#. Result seq11149, hash `cd31c0e66a41e3760331ffd2b159f6ca57244a4d22465829af5cdfbe2d24ca4d`, snapshot `b5750b9dbae119a8e9e301218596d6ee452862479d9b5372f98c699e67350e2b`. Full PGN read back and status verified.

Castled5, developed all minors9, rooks10 and14. First15 moves material-clean. Bd3 was explicitly assessed as blocking Qd1's d4 defense this time, with e3/Nf3 remaining. Equal bishop and queenside-pawn exchanges; Ne2-f4 and Nf3-e5 improved activity. After h4/Nxe5/dxe5, the cleared Bb2 diagonal did protect e5 as planned.

Missed threats:
- ...Qb7 directly attacked Bb2. I annotated hxg5 as a knight-for-pawn gain while looking at other queen lines, overlooking the actual ...Qxb2. This was a knight/bishop exchange, not a won piece. gxh6/Qxe5 subsequently exchanged pawns equally while retaining an advanced h-pawn.
- Nd3 attacked Qe5, but I overlooked ...Qxe3+ before the queen exchange. Qxe3/Rxe3 left White one pawn down. Nd3 also blocked the Rd1-d4 defense of the queen; simply moving the king would not have preserved that queen.
- Rh1 correctly guarded h6; Black Kh7 could not capture it while the rook line remained clear. Kf2 and later f4/g3/Rce1 were legal defensive/activation moves, but the claimed safety of Kf3 was only a current-square check, not a check of the opponent's forcing reply.

Decisive mate: after ...Re2+, 37.Kf3 allowed ...R8e3#. Re2 protected the checking Re3 and controlled f2/g2; White's own f4 and g3 pawns occupied escapes, Black f5 controlled g4, and the e-file/central pawns covered the remaining exits. Re2 also blocked Re1 from capturing the checking rook on e3. No king capture of Re3 was legal while Re2 survived. I had considered a rook exchange but chose king activity without recognizing this mate. This is direct recurrence of trial18's forcing-king-safety target, despite legal move submissions and some correctly identified individual recaptures.

Actual ending had White Kf3/Re1/Rh1/Nd3/a4,c5,f4,g3,h6 versus Black Kh7/Re2/Re3/Bc7/a5,c6,d5,f5,f6,g6. No conversion or improved strength established.

Cumulative51W/3D/81L after135. MAX0W/2D/44L (46); skill0 38W/1D/6L (45); nominal1800 13W/0D/31L (44). Elo1570 [1450,1690], 95% Bayesian equal-tail interval,89 rated games total/latest50,46 MAX excluded. Storage37,248,796bytes. Trial18 now0W/0D/3L; finish the predeclared136–138 before its full endpoint review. No extra practice or changed opponent settings.

## Benchmark 136 — Black versus skill0 — win, 2026-10-03 00:01 UTC

57 own moves,114 plies,zero illegal submissions; actual57...Ra1#. Result seq11265, hash `aed2703c3b4b98a288233bb33a2870713b5a53fec3bc3497de0aad9b6a075395`; snapshot `1c03cbc0806d91580dbe392afc43fc3e8a3c123280dda474dafb2241ad0eb237`. Full PGN and status read back.

Castled5, all minors developed8. First15 own moves had equal material transactions without unexpected loss. Rxa8/Qxa8 and Nxe4/fxe4 were correctly recaptured; fxe4 opened the f-file and drove Nf3 back. Ba6 was protected by Qa8, and Bxa6/Qxa6 later exchanged bishops equally. h6 created a currently safe h7 escape, explicitly conditional on e4 still blocking Qc2-h7. Qe6 restored d5 defense after e6-e5; Qg4's g3 pin was explicitly dropped from the assessment when Qh5 moved away. Queens exchanged25...Qxe2/Nxe2.

White's c6 advance attacked Nd7. Nb8 attacked that pawn; after White Rd1 failed to defend it, Nxc6 won it. Rb8 pressured Bb2; dxe5/Nxe5/Bxe5/Bxe5 was an actual equal minor/pawn exchange leaving R+B versus R+N and a pawn extra. Be5 guarded c7. Kf7-e6-d6 activated the king and kept d5 defended while facing rook/knight checks.

Concrete forcing-safety execution:
- Rb7 blocked Ra7+ with Kc7 support. After Ne6+, Kd6 would have abandoned Rb7; Kb6 was chosen instead, retaining that support.
- White39.Ra6+ left the checking rook unprotected by Ne6. Actual39...Kxa6 was legal and won it; all remaining White defenders were considered, rather than proximity alone.
- White40.Nxc5+ forked king and Rb7. Kb6 retained a legal recapture after a possible Nxb7. White instead continued Na4+, met by Kc6.
- Rb4 attacked Na4 while covering b2/b6, Be5 covered c3 and Kc6 covered c5. White g4 left the knight, and actual Rxa4 won it.

The decisive rook and knight losses were opponent blunders. Correctly taking them and preserving material is observed execution, not independent proof of increased strength. Conversion: hxg5/hxg5/g6 blocked the pawn; ...exf3+ en passant removed the attacking f-pawn with an explicitly allowed Kxf3 recapture. The remaining pawns were captured, the rook cut off ranks, the king advanced, and Ra2-a1# was completed with Ke3 covering d2/e2/f2. No claimed conversion was left hypothetical.

Cumulative52W/3D/81L after136. MAX0W/2D/44L from46; skill0 39W/1D/6L from46; nominal1800 13W/0D/31L from44. Elo1580 [1460,1700],95% Bayesian equal-tail interval,90 rated total/latest50,46 MAX excluded. Storage37,661,248bytes. Trial18 is1W/0D/3L through four games; finish the unchanged137–138 nominal1800 pair before full assessment. The prior checkmate in135 and defender errors remain in the trial record.


## Benchmark 137 — 2026-10-03 00:22 UTC
White versus nominal 1800; loss by resignation after 53...Rg2. 53 own moves, 106 plies, zero illegal submissions. Full saved PGN read. Result seq 11373; hash b20c02b1fe0703b412366ca9b86abeffc9880be69d01e2438b0b29672685c4bc; snapshot 034181d05c880a08d61abe15a206114af281b142d9e151116f78ad6dcae4d898.

Castled on 5, last minor developed/exchanged by 10, rooks activated on 11 and 15; first 15 moves had no unexpected material loss. The supported Nd6 outpost and Rc5 activity won the a-pawn. Qd3 retained Bb3 and d6 defenses; R1c3 added a lower-value bishop defender against Qb6/Rb8, correctly avoiding an insufficient queen-only recapture. Rxc6 won a second pawn and d7 created a serious passer. However, the proposed queen-exchange/Rc8 conversion omitted 36...Ne2+, a checking fork of king and supporting rook. 37.Kh2 Nxc3 38.Rxc3 left rook and bishop versus two rooks, with two extra pawns. This was an unanticipated exchange loss, not an independently validated sacrifice.

Ba4, Rd3 and b3 retained the passer/bishop; the king reached e4. The specific break 47.f5 gxf5+ 48.gxf5 exf5+ 49.Kxf5 actually occurred, and the king capture was legal only after both adjacent pawn defenders had left. 51.Kxh5 was also legal and gained another pawn. Then 52.Rg3 was a decisive fresh blunder: after ...Rxg3 I had imagined h3xg3, a sideways pawn capture. The pawn could only capture g4. No illegal attempt was submitted, but the rook was lost for nothing. This repeats elementary capture-origin failure despite earlier practice on related geometry. Final position after Kh4/Rg2: White Kh4/Ba4 with b3,d7,e5,h3 against Black Ke7/Rd8/Rg2/f7. I resigned as a practical assessment with legal continuations remaining; no forced loss was proved.

Cumulative 52W/3D/82L in 137; nominal 1800 13W/0D/32L in 45. MAX 0W/2D/44L in 46; skill 0 39W/1D/6L in 46. Elo 1570 [1450,1690], 91 rated total/latest 50 and 46 MAX excluded. Storage 38,068,679 bytes. Trial 18 through 133–137: 1W/0D/4L, 215 own moves/431 plies, zero illegal submissions. Actual positive king-capture evidence did not prevent a forcing-check miss or a basic impossible recapture plan. No sustained improvement claim; finish predeclared game 138 before assessment.


## Benchmark 138 — 2026-10-03 00:46 UTC
Black versus nominal 1800; loss by resignation after 54.Kg6. 53 own moves, 107 plies, zero illegal submissions. Full saved PGN read. Result seq 11482; hash 470daa651f1a6f73320e06eb0ff9d69da9572f0a7ebc15f04930c9972c3d3e2e; snapshot 2262911ee3f21c3bfad8fc2c616ce53fcd3c47bdc0beb7838a023cbda3a752fa.

Castled on 6, minors developed by 10, rooks active on 9/14; first 15 moves were material-clean. Queens exchanged on 12. Nxd3/cxd3 was an equal minor exchange; c6 retained the attacked c-pawn. Nxc3/Rxb7 exchanged pawns, then Nxe6/Rxe6/Rxe6/fxe6 exchanged minors and rooks equally. The f7-to-e6 pawn capture was actually legal and executed. Rxd3 won a pawn. After Be5, I recognized that the bishop made a king capture of a rook on g7 illegal; Nf5 added an effective defender. Rd5 supported a5, but Bc3 added a second attacker, so I did not assume Rxa5 would be a safe recapture. The king became active; 36...Kxd5 after Rxd5+ was an actual legal rook recapture, with surviving bishop/pawn controls checked.

The minor-piece ending deteriorated despite these local successes. After Kf2 I recognized that Nxf3 no longer won a pawn because the king defended it. ...g5 supported the restricted Nh4, Bxa5 returned material to equality, Kxa4 gained a pawn, and fxg5/hxg5 preserved the knight's pawn defender. White's Ke3 allowed the actual escape ...Ng2+ and ...Nf4. However, king activity and pawn grabs did not produce a coordinated conversion: Kxe5 removed the central pawn; Nxg4+/Kxg5 left one pawn each. White's bishop and king dominated the knight's route to the h-pawn. Several proposed knight routes were rejected mentally because the bishop or king could capture; Nd7/Bg7 also closed the f8 route. The c-pawn did not advance in time. Final: Black Kc4/Ne4/c6 against White Kg6/Bg7/h6. I resigned because I could not find a viable promotion defense; no tablebase/engine evaluation or exhaustive forced-loss proof was used. This is an endgame coordination and race failure, not a checkmate or illegal submission.

Cumulative 52W/3D/83L in 138. Each opponent has 46 games: MAX 0W/2D/44L; skill 0 39W/1D/6L; nominal 1800 13W/0D/33L. Elo 1560 [1440,1680], 92 rated total/latest 50; 46 MAX excluded. Storage 38,470,080 bytes.

## Trial 18 fixed endpoint — 138
All predeclared study and practice bounds were respected; no extra practice was added after the failed fresh practice. Benchmarks 133–138: 1W/0D/5L, 268 own moves/538 plies, zero illegal submissions. MAX 0/2, skill 0 1/2, nominal 1800 0/2; White 0W/3L, Black 1W/2L. All six had material-clean first 15 moves. Baseline 1580 [1460,1700] became 1560 [1440,1680]. Intervals overlap; this is not a statistical proof of decline, but there is no measured improvement.

Remembered contrast predictions matched mechanical legality, which is retention evidence only. The two fresh practices were unfinished: one pawn up with an unresolved rook attack, one pawn down with an unresolved pinned bishop. Benchmark positives include the actual Kxa6 capture and conversion in 136, Kxf5/Kxh5 in 137, effective g7 defense and Kxd5 in 138. They do not establish reliable transfer: 135 ended in the targeted forcing-check mate, 137 omitted ...Ne2+ and then lost a rook through an impossible sideways pawn-recapture assumption, while 133/134 retained defender and exchange errors. 138 added an unresolved knight-versus-bishop pawn-race weakness. Decision: discontinue the current king-safety cue as a successful intervention; retain ordinary development, acknowledge prior material-geometry methods also failed, and predeclare a revised bounded learning period before games 139–144. The 200-scored-game endpoint remains unchanged; 62 scored games remain.
