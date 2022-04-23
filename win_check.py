def win_check (board, mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark) or 
      (board[6] == mark and board[5] == mark and board[4] == mark) or 
      (board[3] == mark and board[2] == mark and board[1] == mark) or 
      (board[9] == mark and board[6] == mark and board[3] == mark) or 
      (board[8] == mark and board[5] == mark and board[2] == mark) or 
      (board[7] == mark and board[4] == mark and board[1] == mark) or 
      (board[9] == mark and board[5] == mark and board[1] == mark) or 
      (board[7] == mark and board[5] == mark and board[3] == mark)) 