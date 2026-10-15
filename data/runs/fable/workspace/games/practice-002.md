# Practice 2 — White vs practice-skill-0 — LOSS (0-1, checkmate, 66 plies, 2 illegal attempts)

Moves: 1. d4 e6 2. Bf4 d5 3. e3 c5 4. c3 a6 5. Nf3 Nf6 6. Bd3 c4 7. Bc2 b5 8. O-O Be7 9. Nbd2 Bb7 10. Ne5 a5 11. Qe2 Nc6 12. Nxc6 Bxc6 13. e4 Nxe4 14. Nxe4 dxe4 15. Bxe4 Bd5 16. Bxd5 exd5 17. Rfe1 Ra7 18. Qe5 Kf8 19. Bg3 b4 20. cxb4 Bxb4 21. Rec1 h5 22. a3 Bd2 23. Rd1 Re7 24. Qf5 h4 25. Bxh4 Rxh4 26. Rxd2 Re6 27. g3 Rhe4 28. f3 Re2 29. Rxe2 Rxe2 30. Qf4 Rxb2 31. Qf5 c3 32. Rc1 Qe8 33. Rxc3 Qe1# 0-1

## What happened
- Opening/middlegame fine: level, then won a pawn (25.Bxh4! Rxh4 26.Rxd2 — the tempo on e7 made the bishop-for-pawn capture work).
- Move 29-31: traded rooks; Black's rook reached my 2nd rank and took b2 (level). Black's c-pawn ran to c3.
- 32.Rc1 attacked c3. Black replied 32...Qe8, which quietly threatened Qe1# (e-file open, my Rc1 the ONLY guard of rank 1, Black's Rb2 covering f2/g2, my own f3 pawn blocking Qf5-f1).
- 33.Rxc3?? took the "free" pawn and removed the back-rank guard. 33...Qe1# .

## Error classes (self-assessed)
1. **Skipped scan on a "free" capture** (decisive). I did not write the A-D lines for 33.Rxc3; line C would have found Qe1+ with no legal reply. Same class as G5 31.Nxa8?? and practice 1's planned "block". The scan works when written; it is skipped exactly when a move looks obviously good.
2. **Back-rank guard**: moving the sole guard of my first rank while an enemy heavy piece has an open file to it. Needs an explicit check: "which of my pieces guard the checking squares on my back rank, and is this move removing one of them?"
3. Two illegal submissions: 24.Qc5 (path blocked by Black's d5 pawn) and 31.Qh5 (f4-h5 is not a queen line). Both were geometry slips during long analysis, not legality-rule errors. Need a last-step geometry re-check of the submitted move.
4. Evaluation drift: after 30...Rxb2 (level) I spent a long time on attacking ideas (Qh8# patterns) while Black's counterplay (Re2/Qe3+ mating ideas, then the c-pawn) was the real issue; fine, but the tie-up cost time and attention.

## Scan successes in this game (the method is useful when applied)
Rejected 10.e4? (recapture hangs), 18.Bg5?, 19.Bh6?/Bh4?, 21.Qc5+?? (b4 bishop covers c5), 29.Qxe6?? (both Black rooks connected on the e-file — Rxe6 would have won my queen), 30.Qe5?? (queen "defended by d4" but a rook takes a queen), 31.Qh6?? (g7 pawn covers h6), Qd3?? (c4 pawn), Re2?? (Re6xe2 undefended). About 9 one-move blunders avoided by writing the lines.

## Decision
Keep the scan; make it unskippable (procedure v2.2): the four lines are written for EVERY move including captures and recaptures; add the back-rank guard question to line C; add a geometry re-check before typing the UCI.
