from collections import defaultdict

def solution(a):
    if len(a) < 2 :
        return 0
    
    counter = defaultdict(int)
    a = [a[0]] + a + [a[-1]]
    used = [-1] * (len(a))
    
    for i in range(1, len(a)-1) :
        if a[i] != a[i-1] and used[i-1] != a[i] :
            counter[a[i]] += 1
        elif a[i] != a[i+1] :
            used[i+1] = a[i]
            counter[a[i]] += 1
    
    if len(counter) < 2 :
        return 0
    return max(counter.values()) * 2