def solution(arr):
    answer = [0, 0]
    
    def dq(pr, pc, size) :
        initial = arr[pr][pc]
        for r in range(pr, pr+size) :
            for c in range(pc, pc+size) :
                if arr[r][c] != initial :
                    break
            else :
                continue
            break
        else :
            answer[initial] += 1
            return
        
        half = size//2
        dq(pr, pc, half)
        dq(pr, pc+half, half)
        dq(pr+half, pc, half)
        dq(pr+half, pc+half, half)
        
    dq(0, 0, len(arr))
    return answer