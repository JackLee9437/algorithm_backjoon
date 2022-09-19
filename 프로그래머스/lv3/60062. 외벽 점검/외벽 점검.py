def solution(n, weak, dist):
    answer = len(dist)+1
    
    def dfs(start, cur, dists, count) :
        nonlocal answer, n
        for i in range(len(dists)) :
            j = cur
            b = weak[j] + dists[i]
            while weak[j] <= b :
                j += 1
                if j == start :
                    answer = min(answer, count+1)
                    return
                elif j == len(weak) :
                    j = 0
                    b -= n
            tmp = dists[:]
            tmp.pop(i)
            dfs(start, j, tmp, count+1)
    
    for s in range(len(weak)) :
        dfs(s, s, dist, 0)
        
    if answer == len(dist)+1 :
        return -1
    return answer