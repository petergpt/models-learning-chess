# Current move procedure — trial 05

Unproven execution change: reason from the opponent's turn before pursuing a distant plan. Trial 04 is archived in `trials/move-check-before-05.md`; successful practice does not establish stronger play.

1. Read the actual board and reconstruct the candidate by clearing its origin, removing any capture and filling its destination. Retain the actual king and queen squares. If already in check, the reply must remove every checking line. Immediate captures of the moved piece, including either pawn origin, still matter.
2. Choose the opponent's most concerning immediate forcing reply yourself: a check, capture, fork or attack on a defender. Carry that concrete branch through the actual required recapture, then stop and rebuild the resulting position before any remote continuation. State which defender moved or disappeared and where its replacement now stands. If no exchange is relevant, test the direct threat on the candidate's resulting board instead. Do not substitute a statement that a scan was done for an actual reply and answer.
3. From that rebuilt position, test the opponent's next check, fork or major-piece capture. A defense which existed before the exchange must be established again. Reject an unresolved immediate loss and restart if the candidate changes. Keep this first branch short; lengthy alternate lines must not displace this concrete check before submission.

Game 54 reminder: Rd8 could capture Nd7 before Rxf8+/Rxf8; afterward that rook was on f8, where Nd7 attacked it and Qe5 while clearing Qa3's diagonal. Moving the queen to g6 instead leaves a rook escape in the supplied practice line. That line is not a proof of a best move.

Other concrete hazards: a knight's departure may open a second check; a pawn's departure can expose a queen; a king recapture must be legal; a rook route can still contain an own pawn. No automated analysis, move menu, search, scoring or delegated move selection is permitted.
