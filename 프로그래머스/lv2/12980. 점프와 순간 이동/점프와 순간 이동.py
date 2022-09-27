def solution(n):
    ans = 0
    q, r = divmod(n, 2)
    while q :
        ans += r
        q, r = divmod(q, 2)
    ans += r

    return ans