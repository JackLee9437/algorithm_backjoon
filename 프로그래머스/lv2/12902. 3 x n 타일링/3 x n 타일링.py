def solution(n):
    if n & 1 : 
        return 0
    mod = int(1e9) + 7
    
    n //= 2
    dp = [0] * (n+1)
    dp[1] = 3
    dp[2] = 11
    
    for i in range(3, n+1) :
        dp[i] = dp[i-1] * 3 + 2
        for j in range(1, i-1) :
            dp[i] += dp[j] * 2

    return dp[n] % mod
    
    