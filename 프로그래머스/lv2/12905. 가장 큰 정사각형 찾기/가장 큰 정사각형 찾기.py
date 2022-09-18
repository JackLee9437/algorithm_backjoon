def solution(board):
    answer = 1
    
    if len(board) == 1 :
        if sum(board[0]) :
            return answer
        return 0
    elif len(board[0]) == 1 :
        if sum(zip(*board)) :
            return answer
        return 0
    
    m, n = len(board), len(board[0])
    
    for r in range(1, m) :
        for c in range(1, n) :
            if board[r][c] and board[r-1][c-1] :
                if board[r-1][c] and board[r][c-1] :
                    board[r][c] = min((board[r-1][c-1], board[r-1][c], board[r][c-1])) + 1
    
    return max(max(x) for x in board) ** 2
            
            