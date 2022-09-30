from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[1] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle :
        for x in range(x1*2, x2*2+1) :
            for y in range(y1*2, y2*2+1) :
                board[x][y] = 0
    for x1, y1, x2, y2 in rectangle :
        for x in range(x1*2+1, x2*2) :
            for y in range(y1*2+1, y2*2) :
                board[x][y] = 1
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    dirx = [[1,0],[0,1],[-1,0],[0,-1]]
    que = deque([(characterX, characterY)])
    board[characterX][characterY] = 1
    while que :
        x, y = que.popleft()
        if x == itemX and y == itemY :
            break
        for dx, dy in dirx :
            nx = x + dx
            ny = y + dy
            if not board[nx][ny] :
                board[nx][ny] = board[x][y] + 1
                que.append((nx, ny))
            
    return board[itemX][itemY] // 2
            