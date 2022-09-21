def solution(line):
    intersections = set()
    for i in range(len(line)-1) :
        for j in range(i+1, len(line)) :
            A, B, E = line[i]
            C, D, F = line[j]
            if A*D-B*C != 0 :
                denominator = (A*D-B*C)
                x = (B*F-E*D)/denominator
                if x == int(x) :
                    y = (E*C-A*F)/denominator
                    if y == int(y) :
                        intersections.add((int(x), int(y)))
    buf = []
    leftmin, _ = min(intersections, key=lambda x: x[0])
    _, bottommin = min(intersections, key=lambda x: x[1])
    rightmax = 0
    upmax = 0
    for intersection in intersections :
        x = intersection[0]-leftmin
        y = intersection[1]-bottommin
        buf.append((x, y))
        rightmax = max(rightmax, x)
        upmax = max(upmax, y)
    
    answer = [['.' for _ in range(rightmax+1)] for __ in range(upmax+1)]
    for x, y in buf :
        answer[upmax-y][x] = '*'
        
    return list(map(lambda x : ''.join(x), answer))