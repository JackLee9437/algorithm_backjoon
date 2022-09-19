def solution(n):
    answer = 0
    
    rightUp = [0] * (2 * n - 1)
    rightDown = [0] * (2 * n - 1)
    vertical = [-1] * n
    
    def nQueen(c) :
        nonlocal answer, n
        if c == n :
            answer += 1
            return
        
        for r in range(n) :
            if r in vertical or rightUp[r+c] or rightDown[n+r-c-1]:
                continue
            vertical[c] = r
            rightUp[r+c] = rightDown[n+r-c-1] = 1
            nQueen(c+1)
            vertical[c] = -1
            rightUp[r+c] = rightDown[n+r-c-1] = 0
        
    nQueen(0)
    return answer
    
    
    return answer