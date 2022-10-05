from collections import deque

def solution(alp, cop, problems):
    alpMax, copMax = max(problems, key=lambda x : x[0])[0], max(problems, key=lambda x : x[1])[1]
    problems.sort()
    dp = [[int(1e9)] * 151 for _ in range(151)]
    dp[alp][cop] = 0
    
    que = deque([(alp, cop, 0)])
    while que :
        algoPower, codePower, time = que.popleft()
        if (algoPower >= alpMax and codePower >= copMax) or dp[alpMax][copMax] < time :
            continue
        if dp[algoPower][codePower] < time :
            continue
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
            if alp_req > algoPower :
                break
            if cop_req <= codePower :
                tmp_alp = min(150, algoPower+alp_rwd)
                tmp_cop = min(150, codePower+cop_rwd)
                tmp_time = time+cost
                if dp[alpMax][copMax] <= tmp_time:
                    continue
                if dp[tmp_alp][tmp_cop] > tmp_time :
                    dp[tmp_alp][tmp_cop] = tmp_time
                    que.append((tmp_alp, tmp_cop, tmp_time))

        if algoPower < 150 and dp[algoPower+1][codePower] > time+1 :
            dp[algoPower+1][codePower] = time+1
            que.append((algoPower+1, codePower, time+1))
        if codePower < 150 and dp[algoPower][codePower+1] > time+1 :
            dp[algoPower][codePower+1] = time+1
            que.append((algoPower, codePower+1, time+1))
        
    
    for r in range(150, alpMax-1, -1) :
        for c in range(149, copMax-1, -1) :
            dp[r][c] = min(dp[r][c], dp[r][c+1])
    
    for c in range(150, copMax-1, -1) :
        for r in range(149, alpMax-1, -1) :
            dp[r][c] = min(dp[r][c], dp[r+1][c])
    
    return dp[alpMax][copMax]