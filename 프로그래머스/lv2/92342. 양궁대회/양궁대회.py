def solution(n, info):
    candidates = []
    diffmax = 0
    minscoreidx = 0
    
    def dfs(n, minidx=0, idx=0, arr=[]) :
        nonlocal candidates, diffmax, minscoreidx
        if idx == 11 :
            ryan = 0
            apeach = 0
            for i in range(11) :
                if arr[i] :
                    ryan += 10 - i
                elif info[i] :
                    apeach += 10 - i
            scorediff = ryan - apeach
            if scorediff > 0 :
                if candidates :
                    if diffmax < scorediff :
                        diffmax = scorediff
                        candidates = [arr]
                        minscoreidx = minidx
                    elif diffmax == scorediff :
                        if minscoreidx < minidx :
                            candidates = [arr]
                            minscoreidx = minidx
                else :
                    diffmax = scorediff
                    candidates.append(arr)
            return
        
        if idx == 10 and n != 0 :
            dfs(0, minidx, idx+1, arr+[n])
        else :
            dfs(n, minidx, idx+1, arr+[0])
            if (tmp:= info[idx]+1) <= n :
                dfs(n-tmp, idx, idx+1, arr+[tmp])
    
    dfs(n)
    print(candidates)
    if candidates :
        return candidates[0]
    else :
        return [-1]