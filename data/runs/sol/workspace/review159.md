# Benchmark 159 and trial 266

159 White versus skill 0: win by 30 Qg7#, 59 plies, zero illegal submissions. Result seq 12706, 2026-10-09T23:37:47.361068+00:00. Every move chosen mentally; no outside assistance.

15 Qe1 cleared the d-file; 16 Na4 met b4 with a protected knight and queen attack; 17 Rxd6 won a pawn, 18 Rdd1 retreated from Be5. 19 Bxe5 Nxe5 20 f4 Ng6 21 f5 forked bishop e6 and knight g6. 22 fxe6 Nxe2+ 23 Qxe2 gained a minor. 24 Rd7 Qxa4 25 bxa4 was a major opponent gift: the knight remained protected by b3. Further Re7 and Rf7 allowed both rooks to be captured. 29 Qxg5+ Kh8 30 Qg7# finished with the queen protected by Rf7. No major-piece loss from stale defenders in this game, but the opponent gifts make a general improvement claim unjustified.

Verified totals: 159 scored, 44 wins, 8 draws, 107 losses. Full strength 0/0/54; skill 0 37/4/12; nominal 1800 7/4/41 (W/D/L). Provisional engine-relative Elo 1550, conditional 95% credible interval [1420,1670], latest 50 rated games; 105 rated total, 54 uncalibrated full-strength games excluded. Nominal anchors and model assumptions; not human/platform Elo. One weak-opponent win and a ten-point estimate increase do not establish learning.

## Learning period: trial 266

Weakness: in 158, bishop withdrawal to h7 led to a rook on h7 after a bishop exchange, then the rook became exposed and its escape path was blocked by my own later bishop development. Try a retreat that preserves ordinary development and the rook at home. Observable transfer: develop without an early exposed rook or a major-piece loss caused by changed defenders/blocked escape paths. Formal benchmark review remains 162.

Mental review of the remembered position after 5 g4: Bd7 is reachable via empty e6; after e6, e5 still attacks d6 and f6, so Bd6 and Nf6 would put pieces on pawn-attacked squares. Bb4 develops the other bishop instead.

Recorded practice 139, maximum opponent, Black from benchmark 158 ply 9: Bd7 Be3 e6 Nc3 Bb4 Ne2. Stopped after three own moves, six plies, zero illegal submissions; unfinished, excluded from Elo. Result seq 1370, 2026-10-09T23:38:39.115490+00:00. All material retained, rook h8 stayed home, bishop f8 developed. A short remembered-position repair only; no proof of equality, safety over a full game, or transfer. Return next to benchmark 160, Black versus skill 0, then 161–162 nominal 1800.
