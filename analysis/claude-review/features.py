from load import *
def feats(x):
    s=x['start']; learner = s['color']=='white'
    board=chess.Board(s.get('initial_fen', chess.STARTING_FEN))
    bal=[mat(board,learner)]; own=[]; caps=[]
    for i,m in enumerate(x['moves']):
        mv=chess.Move.from_uci(m['uci'])
        actor='model' if board.turn==learner else 'sf'
        pc=board.piece_at(mv.from_square); tg=board.piece_at(mv.to_square)
        if actor=='model': own.append((m['san'],pc.piece_type, board.is_castling(mv)))
        if actor=='sf' and tg and tg.color==learner and tg.piece_type not in (chess.PAWN,chess.KING):
            caps.append(i)
        board.push(mv); bal.append(mat(board,learner))
    losses=0
    for i in caps:
        if i==0 or i+1>=len(x['moves']): continue
        if bal[i+2]-bal[i-1] <= -2: losses+=1
    castle=[j for j,(san,pt,c) in enumerate(own,1) if c]
    return dict(own=len(own), shortloss=losses, final_bal=bal[-1], min_bal=min(bal),
                max_bal_after20=max(bal[20:]) if len(bal)>20 else None,
                castle10=(bool(castle and castle[0]<=10) if len(own)>=10 else None),
                first=own[0][0] if own else None, sig=' '.join(o[0] for o in own[:4]),
                white_first=x['moves'][0]['san'] if x['moves'] else None)
