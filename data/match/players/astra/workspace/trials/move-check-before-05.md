# Current move procedure — trial 04

This replaces the destination-only execution change. It is an unproven method, not a claim of improvement. The longer reference is preserved in `trials/move-check-before-04.md`.

1. Read the actual board. Locate my king and queen, and the opponent's queen, rooks, bishops and nearby knights. If I am in check, identify every checking line before considering a capture or block. A knight move may have opened a second line from its origin.
2. Choose a candidate, then reconstruct only its immediate resulting board: clear the origin, remove any captured piece, and fill the destination. Trace enemy bishop, rook and queen lines through the squares that changed, starting with any line reaching my king or queen. Then inspect immediate captures of the moved piece, including both pawn origins. Record this short factual result internally before pursuing a longer continuation. A still-blocked line and a newly opened line must not be treated as the same position.
3. Test the opponent's forcing reply from that reconstructed position. Scan immediate checks and nearby knight forks; a king move must survive the opponent's next check, and a defensive capture must remove all existing checks. Carry an exchange only through the actual legal recapture needed for the decision. If the candidate changes, repeat the reconstruction. Before submission, return to this record instead of reusing an earlier branch's board.

Stop a candidate as soon as this reconstruction finds an unaccounted immediate loss; do not continue remote variations as a substitute. The trace must be performed for quiet moves and pawn moves as well as captures and major-piece moves. No automated attack generation, search, scoring or move selection is permitted.

Concrete reminders: game 48's e5-d4 removed the blocker on Bg3-f4-e5-d6 and lost Qd6. Game 47's Nd4-f3 opened Qd5-d4-d3-d2 as well as checking with the knight; Rxf3 could remove only one checker. King support of a recapture still requires a legal destination. Known examples do not establish transfer.
