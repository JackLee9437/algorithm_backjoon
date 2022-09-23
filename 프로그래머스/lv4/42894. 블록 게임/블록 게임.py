def solution(board):
    n = len(board)
    
    dirx = [[1,0],[0,1],[-1,0],[0,-1]]
    erased = set([0])
    for _ in range(200) :
        flag = True
        for c in range(n) :
            for r in range(n) :
                if board[r][c] in erased :
                    continue
                
                que = [(r,c)]
                i = 0
                while i < len(que) :
                    cr, cc = que[i]
                    for dr, dc in dirx :
                        nr = cr + dr
                        nc = cc + dc
                        if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in que and board[nr][nc] == board[r][c] :
                            que.append((nr,nc))
                    i += 1
                minr, minc = min(que, key=lambda x : x[0])[0], min(que, key=lambda x : x[1])[1]
                maxr, maxc = max(que, key=lambda x : x[0])[0], max(que, key=lambda x : x[1])[1]
                empty = []
                for cr in range(minr, maxr+1) :
                    for cc in range(minc, maxc+1) :
                        if board[cr][cc] != board[r][c] :
                            empty.append((cr, cc))
                
                for i in range(2) :
                    cr, cc = empty[i]
                    for nr in range(cr, -1, -1) :
                        if board[nr][cc] not in erased :
                            break
                    else :
                        continue
                    break
                else :
                    erased.add(board[r][c])
                    flag = False
                    continue
                break
        if flag :
            break
                
    return len(erased) - 1