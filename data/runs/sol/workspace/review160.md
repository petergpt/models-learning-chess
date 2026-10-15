# Benchmark 160 and learning trial 267

160 Black versus skill 0: win by 42 Qxb2#, 84 plies, one illegal submission. Result seq 12793 at 2026-10-09T23:47:35.682886+00:00. Every move chosen mentally; referee only.

Development: d5, Nf6, e6, Be7, O-O by move five, c5, Nc6, b6, Bb7. Rooks stayed home in the opening. Illegal 10 d5d4: d4 was occupied by White's pawn. Corrected with cxd4. White Nb5 ignored the pawn's second capture, dxe3, and later h6 ignored a6's attack on the knight: axb5 hxg7 Kxg7 won material but exposed my king. 16 Ne4 came with faulty imagined knight geometry: e4 does not attack d3, and removing Nf6 let Rxh7+ occur. Queen d3 protected the checking rook, so I correctly moved Kg8; Qe3 then removed that defender and Kxh7 won the rook. Nxg5 and Bxg5 simplified, with B on g5 protected by Qd8. Avoided repeated bishop checks with Kg7. Bh6 Rxh6 Kxh6 traded a bishop for the remaining rook. Kf8 protected Rg8; Qxg8+ Kxg8 removed the queen. Kxh7 later removed the last bishop.

Conversion error: 37 Rb4 overlooked the a3 pawn's capture square. Qd4 protecting Rb4 did not make a rook-for-pawn trade good. White axb4 forced Qxb4. Na5, Qb3, Nc4 then supported Qxb2# with the knight; this eventually finished despite the needless rook loss. Result heavily aided by opponent gifts, not proof of sound play or corrected pawn geometry.

Verified totals: 160 scored, 45W 8D 107L. Full strength 0/0/54, skill0 38/4/12, nominal1800 7/4/41. Provisional engine-relative Elo 1560, conditional 95% credible interval [1440,1680], latest 50 rated of 106; 54 uncalibrated maximum games excluded. Not FIDE/platform Elo; estimate/model/anchors do not establish sustained improvement. Formal review remains 162.

## Trial 267: repair rook conversion

Weakness: confusing a protected major piece with immunity to a cheaper pawn capture; failing to recompute pawn capture squares. Test a knight route and keep the rook out of a3's attack, then respond to actual opponent pawn changes. Observable transfer: no rook/queen loss to an ordinary pawn capture in 161–162. General improvement not established by a remembered-position drill.

Practice 140, maximum opponent, Black from 160 ply 73 before Rb4: Na5 b3 Rxa3 c4 Qe4+ Kb2 Rxb3+ Kc1. Initially planned three own moves; extended to four because Kb2 attacked the rook on a3. Rxb3+ was protected by Na5. Eight plies, zero illegal submissions, stopped unfinished, seq 1381 at 2026-10-09T23:48:50.258825+00:00. All remaining pieces retained and two pawns captured. b3 changed the a-pawn's defender and attacked Ra4; c4 occupied the proposed knight destination and b3 controlled c4, so I adapted instead of following the original Nc4 plan. This repairs a remembered example over a short horizon only, with no measured score or proved full-game safety.

Next: benchmark 161 White nominal 1800, then 162 Black nominal 1800 and formal review. Retain development/king-safety emphasis but explicitly recognize that castling did not prevent later exposure and that the major-piece pawn-capture weakness recurred.
