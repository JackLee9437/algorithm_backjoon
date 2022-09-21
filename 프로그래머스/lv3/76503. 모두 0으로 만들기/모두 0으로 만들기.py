from collections import deque

def solution(a, edges):
    if sum(a) != 0 :
        return -1
    if sum(1 if x == 0 else 0 for x in a) == len(a) :
        return 0
    
    graph = [set() for _ in range(len(a))]
    for u, v in edges :
        graph[u].add(v)
        graph[v].add(u)
    
    que = deque()
    for i in range(len(a)) :
        if len(graph[i]) == 1 :
            que.append(i)
            
    count = 0
    while que :
        f = que.popleft()
        if not graph[f] :
            continue
        t = graph[f].pop()
        if a[f] != 0 :
            v = a[f]
            a[f] -= v
            a[t] += v
            count += abs(v)
        graph[t].discard(f)
        if len(graph[t]) == 1:
            que.append(t)
    
    if sum(a) == 0 :
        return count
    return -1