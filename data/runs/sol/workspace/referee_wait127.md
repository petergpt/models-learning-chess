# Referee wait during benchmark127

Last confirmed board after19g3/Nxf2: r4rk1/pp3ppp/3qpn2/1Bbp4/3N4/1PP3P1/PB2Qn1P/2R3K1 w - - 0 20.
Submitted ./play move e2f2 once. It returned only t3-job queued(queue_fairness), not referee acceptance. Its exec session metadata was not preserved. Do NOT resubmit blindly.
A follow-up ./play board is running in exec session43946 and also waiting(queue_fairness). Poll that session and inspect actual referee board before selecting any next move. Both commands were launched normally via ./play/t3-job. No bypass or foreign resource inspection.
Game127 active, result unknown. No learning/practice started. Trial205,formal132,endpoint200,goalactive.

Resolved: board confirmed20Qxf2/e5.127 subsequently completed by resignation after22...Ba3,44plies,0illegal. No pending referee command and no duplicate submission.
