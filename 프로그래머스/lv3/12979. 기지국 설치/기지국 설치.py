from math import ceil

def solution(n, stations, w):
    needs = []
    
    installed = 0
    for station in stations :
        if (tmp:= station - w - 1 - installed) > 0 :
            needs.append(tmp)
        installed = station + w
    if (tmp:= n - installed) > 0 :
        needs.append(n-installed)
        
    answer = 0
    rangeSize = 1 + 2 * w
    for need in needs :
        answer += ceil(need / rangeSize)
    
    return answer