# Move check

Working protocol, based on my own recorded errors. No claim of tested improvement.

1. Reconstruct the current position, especially the king, queen, loose pieces, and recently vacated squares. Use the referee board if uncertain. State pawn attack directions correctly.
2. Identify the opponent's immediate checks and captures. A quiet move may have opened a defender behind another piece.
3. Choose a candidate for a concrete purpose. Test the cheapest enemy capture of any valuable exposed piece. Include pawn pushes that attack the candidate's destination, and identify a usable retreat. Calculate exchanges through the last recapture, but treat each recapture as a choice: the opponent may stop trading or move the queen away. Do not call a target safe merely because a queen defends it. Before relying on a defender, check whether the opponent can exchange or displace it first; game 19's ...Bb4 and ...Bxd2 removed the knight needed to hold c4.
4. Reconstruct the position after the candidate. Enumerate the opponent's checks before comparing material threats. For each enemy rook, inspect its reachable intersections with my king's rank and file; also inspect queen, bishop, knight, and pawn checks. Extend a checking ray through my king to any queen or rook behind it. Check paths and pins again, including whether my own king blocks a proposed defensive capture or interposition.
5. For king moves, inspect alignment with my queen and rooks. A king escape can expose a skewer. For a proposed king recapture, verify that the destination is not attacked after the capture. A king beside a piece does not defend it against an attacker supported by another enemy piece.
6. Prefer a verified material gain or sound development to an unverified sacrifice. With a large advantage, preserve coordination and check stalemate before quiet finishing moves.
7. For an exposed king, inspect captures of the checker and interpositions as well as king escapes. Count actual escape squares, including squares occupied by my own pieces. If the checker also protects a queen's mating square, removing it may matter more than keeping that minor piece. When a move uncovers another line, check for double check: capturing one checking piece may leave the other check intact.
8. Before accepting a king escape, inspect queen checks on the new king's rank, file, and diagonals. A queen can switch from a diagonal to a file in one move. Reject immediate mate before comparing material threats.

Keep the final audit focused on the actual candidate and current board. Additional remote variations do not substitute for it.

For a capture or sacrifice, explicitly inspect both enemy pawn origins that could capture the landing square. A white piece on g6 can be taken by a black pawn on f7 or h7; a black piece on g3 can be taken by a white pawn on f2 or h2. In game 21, I examined queen captures and king escapes after Rxg6+ but omitted ...hxg6. Protection against the king's capture did not protect the rook from the pawn.

For an enemy knight near several valuable targets, scan every reachable landing square for a fork; examining one plausible route is insufficient. For a pawn on the seventh rank, examine the forward promotion and both capture promotions separately. Game 20 missed Nd5 after focusing on Nd7, then missed cxb8=Q after examining cxd8=Q+.

When planning a queen exchange, test the opponent's order of captures and any rook check after the queens disappear. Do not assume a pawn recapture comes first. Rebuild the board before reusing a line from another candidate: an unmoved pawn may still occupy the square that the variation had cleared.

Before allowing the final rook exchange, reconstruct the resulting king-and-pawn position and whose turn it is. Check the pawn's advance and the kings' routes to its promotion square. A legal king recapture and a defended rook do not establish a defensible ending; game 18's Rf5+ forced precisely such an adverse transition.

The final audit has three questions: what checks are available after this exact move; can a cheaper attacker take a valuable piece and stop; and is my intended recapture legal? Apply them to the selected move, even if they were considered earlier in a variation. In game 12 I checked some rook checks but omitted Rc7+, which lost a rook; a partial check list did not suffice.
