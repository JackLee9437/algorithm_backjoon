from collections import deque

def solution(board):
    n = len(board)
    que = deque([(0,0,0,1,0)])
    visited = set([(0,0,0,1)])
    
    def dirx(r1, c1, r2, c2) :
        nonlocal n
        ableDirxs = []
        if r1 == r2 : # 가로
            for dc in [-1, 1] :
                nc1 = c1 + dc
                nc2 = c2 + dc
                if 0 <= nc1 < n and 0 <= nc2 < n and board[r1][nc1] != 1 and board[r2][nc2] != 1 and (r1, nc1, r2, nc2) not in visited:
                    visited.add((r1, nc1, r2, nc2))
                    ableDirxs.append((r1, nc1, r2, nc2))
            for dr in [-1, 1] :
                nr = r1 + dr
                if 0 <= nr < n and board[nr][c1] != 1 and board[nr][c2] != 1 :
                    if (nr, c1, nr, c2) not in visited :
                        visited.add((nr, c1, nr, c2))
                        ableDirxs.append((nr, c1, nr, c2))
                    if (r1, c1, nr, c1) not in visited :
                        visited.add((r1, c1, nr, c1))
                        ableDirxs.append((r1, c1, nr, c1))
                    if (r2, c2, nr, c2) not in visited :
                        visited.add((r2, c2, nr, c2))
                        ableDirxs.append((r2, c2, nr, c2))
        else : # 세로
            for dr in [-1, 1] :
                nr1 = r1 + dr
                nr2 = r2 + dr
                if 0 <= nr1 < n and 0 <= nr2 < n and board[nr1][c1] != 1 and board[nr2][c2] != 1 and (nr1, c1, nr2, c2) not in visited :
                    visited.add((nr1, c1, nr2, c2))
                    ableDirxs.append((nr1, c1, nr2, c2))
            for dc in [-1, 1] :
                nc = c1 + dc
                if 0 <= nc < n and board[r1][nc] != 1 and board[r2][nc] != 1 :
                    if (r1, nc, r2, nc) not in visited :
                        visited.add((r1, nc, r2, nc))
                        ableDirxs.append((r1, nc, r2, nc))
                    if (r1, c1, r1, nc) not in visited :
                        visited.add((r1, c1, r1, nc))
                        ableDirxs.append((r1, c1, r1, nc))
                    if (r2, c2, r2, nc) not in visited :
                        visited.add((r2, c2, r2, nc))
                        ableDirxs.append((r2, c2, r2, nc))
        return ableDirxs
    
    while que :
        r1, c1, r2, c2, t = que.popleft()
        if (r1 == n-1 and c1 == n-1) or (r2 == n-1 and c2 == n-1) :
            return t
        for nr1, nc1, nr2, nc2 in dirx(r1, c1, r2, c2) :
            que.append((nr1, nc1, nr2, nc2, t+1))