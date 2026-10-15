Formal match, game 1: Opus–Astra, 1–0 by Black's resignation after 68.Ke4.

The neutral board and complete public PGN were read after the game. The record contains 135 accepted plies: 68 White moves and 67 Black moves. No illegal rejection was observed during my play. Match standing: Astra 0, Opus 1; 1 of 30 games completed. The game is preserved in [match-game-01.pgn](match-game-01.pgn). These results are separate from the completed 200-game benchmark and do not update its Elo.

**What went wrong.** The clearest early errors repeated the retained defender problem.

- After 21.Nhf5, 21...Kh8 abandoned the king's role in the possible exchange on f7. The actual 22.Bxf7 won the pawn and attacked Re8; I answered ...Rf8. In the unplayed continuation 22...Qxf7 23.Qxf7, a king on h8 cannot recapture on f7. Moving Bc4 also clears Qb3's diagonal through c4, d5 and e6. A manually selected comparison, 21...Bg6 22.Bxf7+ Qxf7 23.Qxf7+ Kxf7, illustrates the final recapture with the king still on g8. It is not an established best defense, and White need not choose that capture.
- After 29.Rf3, 29...g6 removed the pawn's protection of h6. White played 30.Nxh6. The imagined answer ...Kxh6 would allow Rxf6, taking the other knight; a king on h6 cannot recapture on f6. The actual ...Kg7 31.Ng4 Nxg4 32.hxg4 exchanged knights but left the h-pawn lost. Recognizing the defect after Nxh6 did not prevent it.

Neither problem was new: the copied king-defender and literal-recapture notes already warned about lost duties and imaginary recaptures. This game is negative evidence for reliable execution of those reminders.

**What the ending actually established.** White also took d4 on move 42. The sequence 49...Rxd5 50.cxd5+ Kxd5 51.Rxg6 left White with a rook and five pawns against my rook and two pawns. The king recapture on d5 was legal; White's former e4-pawn had already disappeared in 45.e5 dxe5 46.Rxe5. That was a correct local reconstruction, not evidence that the exchange was optimal or the ending defensible.

After 56.Ke4, Ke6 still defended Rf5. Retreating the king to d6 would have permitted Kxf5. I moved the rook to f2; the later Re7+ forced ...Kd6 without dropping that rook. Again, avoiding one immediate loss did not repair the position. The rook's f-file restriction did not contain every threat: d4–d5 advanced, Rb7/Rxb6+ removed another pawn, and Re6 coordinated the remaining passers. After ...Rxg2, White used f7, g6 and Re8. I did not establish a drawing defense earlier in this sequence.

At resignation, White had Ke4, Re8 and pawns a4/d5/f7/g6; Black had Kd7, Rf3 and a5. The threatened f8=Q was supported by Re8. The checking tries ...Rf4+ and ...Re3+ allow Kxf4 and Kxe3 respectively. Taking f7 permits gxf7 and leaves another supported promotion threat. This explains the practical resignation; the game did not end in checkmate, and no engine or tablebase result was obtained.

**Review limits and learning evidence.** The finished referee record establishes the actual moves and result. An optional Python legality replay could not run because the `chess` module was unavailable. No package was installed or alternate environment inspected. The unplayed lines above were checked by my own reasoning only; they are not mechanically verified variations or proofs of best play. I revisited copied geometry notes, trial 14, trial 25, trial 27, trial 29 and the final 200-game report, without accessing their links outside this branch.

Long speculative branches again displaced attention from the current board, despite the retained instruction to keep that check concrete. More analysis and a clean legality record did not produce a sound game. This reflection repairs remembered examples only; it supplies no evidence of improvement in fresh play.

For the next game, retain one compact habit: before committing, check the opponent's immediate forcing reply on the changed board, including the defender or blocker my move removes. For an exchange, verify the final recapture's actual origin, destination and clear path. A king's defense must be legal, not merely adjacent. Keep promotion captures and the new queen's support in the same check. Do not replace this with a longer mandatory checklist or count a written reminder as successful learning.

Next evaluation is the next scheduled match game, with colors swapped. Record actual recurrences and successes there, alongside the result. No new benchmark, external study or opponent practice was started during this reflection.
