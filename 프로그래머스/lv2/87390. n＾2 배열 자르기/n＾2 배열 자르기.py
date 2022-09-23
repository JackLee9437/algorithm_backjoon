def solution(n, left, right):
    answer = []
    
    for k in range(left, right+1) :
        r, c = divmod(k, n)
        answer.append(max(r,c)+1)
    
    return answer