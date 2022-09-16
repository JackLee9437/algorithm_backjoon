def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for a, b in edges :
        graph[a].append(b)
    
    answer = 0
    def dfs(v=0, sheep=0, wolf=0, visitables=[]) :
        nonlocal answer
        sheep += 1 if not info[v] else 0
        wolf += 1 if info[v] else 0
        if wolf >= sheep :
            return
        answer = max(answer, sheep)
        
        visitables.extend(graph[v])
        for i in range(len(visitables)) :
            new = visitables[:]
            new.pop(i)
            dfs(visitables[i], sheep, wolf, new)
    
    dfs()
    return answer