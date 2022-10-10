from collections import deque

def solution(rc, operations):
    matrix = deque(map(lambda x : deque(x), rc))
    sides = [deque(x[0] for x in rc), deque(x[-1] for x in rc)]
    
    def shiftRow() :
        matrix.rotate(1)
        sides[0].rotate(1)
        sides[1].rotate(1)
    
    def rotate() :
        matrix[0][0] = sides[0][0]
        matrix[-1][-1] = sides[1][-1]
        
        matrix[0].rotate(1)
        sides[1].rotate(1)
        matrix[-1].rotate(-1)
        sides[0].rotate(-1)
        
        sides[1][0] = matrix[0][-1]
        sides[0][-1] = matrix[-1][0]
        
    
    operator = {
        "ShiftRow" : shiftRow,
        "Rotate" : rotate
    }
    
    for opr in operations :
        operator[opr]()
        
    for r in range(len(matrix)) :
        matrix[r][0] = sides[0][r]
        matrix[r][-1] = sides[1][r]
        
    return list(map(list, matrix))