def solution(dirs):
    visitedX = [[0] * 10 for _ in range(11)]
    visitedY = [[0] * 11 for _ in range(10)]
    
    answer = 0
    r, c = 5, 5
    for dirx in dirs :
        if dirx == "D" :
            if r == 10 :
                continue
            if not visitedY[r][c] :
                visitedY[r][c] = 1
                answer += 1
            r += 1
        elif dirx == "U" :
            if r == 0 :
                continue
            if not visitedY[r-1][c] :
                visitedY[r-1][c] = 1
                answer += 1
            r -= 1
        elif dirx == "L" :
            if c == 0 :
                continue
            if not visitedX[r][c-1] :
                visitedX[r][c-1] = 1
                answer += 1
            c -= 1
        else :
            if c == 10 :
                continue
            if not visitedX[r][c] :
                visitedX[r][c] = 1
                answer += 1
            c += 1
    
    return answer
    
    