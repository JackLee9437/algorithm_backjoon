INF = float('inf')

def solution(n, start, a, b, fares):
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for c, d, f in fares :
        graph[c][d] = f
        graph[d][c] = f
    for i in range(1, n+1) :
        graph[i][i] = 0
    
    for i in range(1, n+1) :
        for s in range(1, n+1) :
            for e in range(1, n+1) :
                if s == e :
                    continue
                if graph[s][e] != graph[e][s] :
                    graph[s][e] = graph[e][s]
                    continue
                
                if graph[s][i] != INF and graph[i][e] != INF and graph[s][e] > graph[s][i] + graph[i][e] :
                    graph[s][e] = graph[s][i] + graph[i][e]
    
    minCost = graph[start][a] + graph[start][b]
    for i in range(1, n+1) :
        minCost = min(minCost, graph[start][i] + graph[i][a] + graph[i][b])
    
    return minCost