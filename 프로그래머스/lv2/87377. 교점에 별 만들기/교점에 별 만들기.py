def solution(line):
    intersections = set()
    left, right, top, bottom = float('inf'), -float('inf'), -float('inf'), float('inf')
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
                        x, y = int(x), int(y)
                        left, right, top, bottom = min(left, x), max(right, x), max(top, y), min(bottom, y)
                        intersections.add((x, y))
    buf = []
    for intersection in intersections :
        x = intersection[0]-left
        y = intersection[1]-bottom
        buf.append((x, y))
    right -= left
    left = 0
    top -= bottom
    bottom = 0
    
    answer = [['.' for _ in range(right+1)] for __ in range(top+1)]
    for x, y in buf :
        answer[top-y][x] = '*'
        
    return list(map(lambda x : ''.join(x), answer))