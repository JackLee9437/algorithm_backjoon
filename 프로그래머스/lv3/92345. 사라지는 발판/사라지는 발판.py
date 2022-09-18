def solution(board, aloc, bloc):
    dirx = [[0,1],[1,0],[0,-1],[-1,0]]
    m, n = len(board), len(board[0])
    
    def turn(count, a, b) :
        nonlocal m, n
        flag = count & 1
        r, c = a if flag else b
        if not board[r][c] :
            return False, 0
        retrst = False
        retcnt = 0
        
        board[r][c] = 0
        for dr, dc in dirx :
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 1 :        
                rst, movcnt = turn(count+1, (nr, nc) if flag else a, (nr, nc) if not flag else b)
                if not retrst :
                    if rst :
                        retcnt = max(retcnt, movcnt+1)
                    else :
                        retrst = True
                        retcnt = movcnt+1
                else :
                    if not rst :
                        retcnt = min(retcnt, movcnt+1)
        board[r][c] = 1
        return retrst, retcnt
    
    _, answer = turn(1, aloc, bloc)
    return answer