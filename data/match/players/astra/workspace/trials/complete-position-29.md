# Trial 29 — final bounded review: complete the immediate position

Evaluation: benchmarks 199 and 200 ONLY, the remaining fixed White/Black maximum-strength pair. Stop the entire experiment at 200 scored games. Baseline after198:65W/6D/127L; provisional Elo1400 [1270,1520]. MAX games are excluded by the unchanged rating method, so this pair cannot by itself update that Elo.

Weakness: remembered recapture rules have not reliably survived actual blockers, and a successful promotion in197 immediately stalemated. Keep the decision focused on the resulting concrete position, rather than extending speculative branches.

Bounded activity: at most eight minutes from the declaration timestamp below. Review exactly two remembered cases from my own games:198 before17...Bf5 and197 before46.c8=Q. Compare each played move/sequence with one manually selected alternative, using only reconstruction and legality of explicitly supplied moves. No move generation, search, attack-map code or evaluation. No external study and no opponent-practice game in this final trial. No extra examples, repeats or extensions. Close early when these two comparisons are complete, then play199–200.

These are known positions. Selecting this plan already included mentally considering alternate sequences; this is remembered correction work, not a blind or independent test. Mechanical legal acceptance will establish only legality of the supplied line. A chosen opponent reply does not establish best defense.

Implementation cue: name the immediate reply against the candidate and verify its real line to the target in the resulting position; at a near-terminal move include whether the opponent has any move. Keep this brief. This revises focus within already tried methods, not a newly proven improvement.

Observe in199–200: direct material losses from imaginary defense/abandoned blockers, legality rejections, first-15 material-loss screen, W/D/L and any terminal-position error. Two maximum-strength games are a small descriptive check, not causal evidence or a demand for a win.

Declared: 2026-10-03T17:05:20.547411+00:00; hard study deadline: 2026-10-03T17:13:20.547411+00:00


## Remembered review and closure
Both saved starting positions were reconstructed from my own PGNs. All 15 explicitly supplied plies were legal: 3 played plies and 12 alternative plies, over exactly two remembered cases. No move menu, engine evaluation, search or attack-map code was used. Legality data and the fixed verifier are saved alongside this note.

198, after17.d4: played ...Bf5 Qxf5 loses the bishop because Bf6 blocks Rf8. Chosen ...Bf7 b5 axb5 instead keeps the bishop on f7, actually supported by Rf8 and Qe7, and uses the existing a6 pawn to meet b5. This is one legal selected continuation, not evidence that ...Bf7 is optimal or that White must play b5.

197, before46.c8=Q: the recorded promotion stalemated because all four black pawns were blocked and the king's remaining squares were covered. Chosen line:46.Be7 Kh8 47.c8=Q+ Kh7 48.Qh3+ Kg8 49.Bd8 Kf8 50.Qh8#. The supplied moves are mechanically legal; the final mate annotation is my manual rule assessment, not engine analysis or a separately played practice result. At the end Qh8 checks Kf8, the queen covers e8/g8, Bd8 covers e7, Pf6 covers g7, f7 is occupied, and the black pawns have no moves. The initial black reply was chosen, so this line alone is not a best-defense proof. Crucially, Bd8 deliberately leaves f8 available before the final check instead of making another stalemate.

The reviews repaired known examples only. They do not erase the two benchmark errors, demonstrate generalization, or establish a stronger playing method. No fresh case or opponent practice was added. The next and final evaluation is199–200.

Learning closed: 2026-10-03T17:06:22.099464+00:00; stopped early after the two planned comparisons.


## Benchmark 199 — White versus maximum strength — loss by resignation
Completed 2026-10-03T17:19:23.454171+00:00; 37 own moves / 74 plies; zero illegal attempts. Seq16076, sha25614e3def92b311c963e59a21eddfc9ea2489940e91a8e3fdd3eeb7192b31086e9; snapshotc75587b002479f336c1ff64d1ad8945b7ecffbec37cd70698c311f99d2e1de05. Full PGN read. Castled5, developed minors by7, rook15; first15 without material loss.
The familiar opening was changed with11.Nd5 Nxd5 12.exd5 and13.e4. Material remained level initially, but18.Nd2 abandoned the knight's actual defense of d4;20...exd4 won that pawn. This is recurrence of defender removal after the final review, not evidence that the cue worked. The rook trades and26.Nxg4 Qxe4+27.Qxe4 Bxe4+ were actually even exchanges except for the pawn already lost. I distinguished ...Qxe4+ from the different ...Bxe4+ line rather than blindly recapturing a bishop with the queen.
No direct major-piece loss or terminal-position error occurred. The resulting knight was tied to g4, Black's bishop restricted king routes, and the king penetrated f7-f6-g5-f4-e3-d2-c2. After37...Kxb2 the ending was N+4P versus B+6P with an advanced black d-pawn; I resigned practically. No forced-win proof or engine evaluation was obtained. The clean major-piece record is a local positive, but the pawn-defense failure and poor endgame activity remain.
After199:65W/6D/128L; MAX0/2/65, skill0 51/2/13, nominal1800 14/2/50. Elo unchanged1400 [1270,1520];132 rated, latest50;67 MAX excluded. Storage74,506,059 bytes. Exactly one benchmark remains. No additional study before200; final trial remains fixed199–200.


## Benchmark 200 — Black versus maximum strength — loss by resignation
Completed 2026-10-03T17:30:23.986370+00:00; 21 own moves / 43 plies; zero illegal attempts. Seq16121, sha256217e9632fb0ce4b60b03ec3ef074b3215643c556e95515118244362631f8fa1a; snapshot7ebba9502b615050f6a4255c8240c9a3509cd70ce5dc7604c8e114dec542a64b. Full PGN read. Castled8, minors developed by9, rook10; first15 without material loss.
I chose ...Bb7 rather than the earlier ...Bd7 opening. 15...Ne4 16.Nxe4 dxe4 completed an even knight exchange, but my commentary that Re8 supported e4 was FALSE: White's e5 pawn blocked the line. I corrected that description during play. 17.Ng5 targeted f7 and e4, and ...Qd7 did not stop18.Bxf7+ Kh8. The passed pawn advanced19.e6, chased the queen, and White's queen joined the attack withQh5 andQg6.
At21.Qg6, I recognized the threatQh7 with Ng5 support. The tempting ...hxg5 would open the h-file forQh5, with Bf7 denyingg8. I deliberately chose21...Qxg5 to remove the knight while keeping h6 in place;22.Bxg5 took the queen. This was a knowingly chosen sacrifice under attack, not a claim of best defense or proof that all other moves lose. I resigned with2R+2B+N+6P againstQ+2R+2B+7P. The material deficit and attack justify my practical decision; no forced-win proof or engine evaluation was obtained.
After200:65W/6D/129L; MAX0/2/66 over68, skill0 51/2/13 over66, nominal1800 14/2/50 over66. Elo1400 [1270,1520], latest50 of132 rated games;68 MAX excluded. Referee reports active_game=null and storage75,002,074 bytes. No game201 was started.

## Trial 29 closed — final evaluation199–200
0W/0D/2L;58 own moves /117 plies;0 illegal attempts;2/2 first-15 material-loss screens passed. The final remembered review did not transfer reliably:199 abandoned a pawn's knight defender and lost a minor-piece ending;200 again misstated a blocked rook defense and lost to a king attack, ending in a queen sacrifice. No terminal-position mistake occurred in this pair, but neither reached a conversion test comparable to197. Elo remains1400 [1270,1520] because both games are excluded MAX games. No new learning or benchmark block will be started. The 200-scored-game bounded experiment is finished; the superseded MAX-win target was not achieved.
