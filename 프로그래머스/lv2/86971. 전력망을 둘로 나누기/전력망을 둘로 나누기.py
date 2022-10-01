from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires :
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    def cntDiff(v1, v2) :
        nonlocal n
        visited = [0] * (n+1)
        visited[v1] = visited[v2] = 1
        def bfs(v) :
            que = deque([v])
            cnt = 0
            while que :
                node = que.popleft()
                cnt += 1
                for to in graph[node] :
                    if not visited[to] :
                        visited[to] = 1
                        que.append(to)
            return cnt
        
        return abs(bfs(v1)-bfs(v2))

    answer = 100
    for a, b in wires :
        answer = min(answer, cntDiff(a, b))
    
    return answer