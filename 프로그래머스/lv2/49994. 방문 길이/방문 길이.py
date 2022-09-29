def solution(dirs):
    dirx = {
        "U" : (-1, 0),
        "D" : (1, 0),
        "L" : (0, -1),
        "R" : (0, 1)
    }
    
    answer = 0
    routes = set()
    r, c = 0, 0
    for d in dirs :
        dr, dc = dirx[d]
        if not (-5 <= r + dr <= 5 and -5 <= c + dc <= 5) :
            continue
        routes.add((r,c,r+dr,c+dc))
        routes.add((r+dr,c+dc,r,c))
        r += dr
        c += dc
    
    answer = len(routes) // 2
    return answer
    
    