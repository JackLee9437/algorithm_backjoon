from collections import deque

def solution(game_board, table):
    puzzles = [[] for _ in range(7)]
    n = len(table)
    
    dirx = [[1,0],[0,1],[-1,0],[0,-1]]
    for r in range(n) :
        for c in range(n) :
            if table[r][c] != 1 :
                continue
            
            minr = minc = 51
            maxr = maxc = -1
            que = deque([(r,c)])
            table[r][c] = 2
            size = 0
            while que :
                cr, cc = que.popleft()
                minr = min(minr, cr)
                maxr = max(maxr, cr)
                minc = min(minc, cc)
                maxc = max(maxc, cc)
                size += 1
                for dr, dc in dirx :
                    nr = cr + dr
                    nc = cc + dc
                    if 0 <= nr < n and 0 <= nc < n and table[nr][nc] == 1 :
                        table[nr][nc] = 2
                        que.append((nr,nc))
            puzzle = [[0] * (maxc-minc+1) for _ in range(maxr-minr+1)]
            for i in range(maxr-minr+1) :
                for j in range(maxc-minc+1) :
                    puzzle[i][j] = 2 if table[i+minr][j+minc] else 1
            puzzles[size].append(puzzle)
    
    answer = 0
    for r in range(n) :
        for c in range(n) :
            if game_board[r][c] != 0 :
                continue
            
            size = 0
            que = deque([(r,c)])
            minr = minc = 51
            maxr = maxc = -1
            game_board[r][c] = 2
            while que :
                cr, cc = que.popleft()
                minr = min(minr, cr)
                maxr = max(maxr, cr)
                minc = min(minc, cc)
                maxc = max(maxc, cc)
                size += 1
                for dr, dc in dirx :
                    nr = cr + dr
                    nc = cc + dc
                    if 0 <= nr < n and 0 <= nc < n and game_board[nr][nc] == 0:
                        game_board[nr][nc] = 2
                        que.append((nr,nc))
            
            for idx in range(len(puzzles[size])) :
                puzzle = puzzles[size][idx]
                
                for _ in range(4) :
                    if len(puzzle) == maxr-minr+1 and len(puzzle[0]) == maxc-minc+1 :
                        for i in range(minr, maxr+1) :
                            for j in range(minc, maxc+1) :
                                if game_board[i][j] != puzzle[i-minr][j-minc] :
                                    break
                            else :
                                continue
                            break
                        else :
                            break
                    puzzle = list(map(lambda x : x[::-1], zip(*puzzle)))
                else :
                    continue
                del puzzles[size][idx]
                answer += size
                break
            
    return answer
            
            