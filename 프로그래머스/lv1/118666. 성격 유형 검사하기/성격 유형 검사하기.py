def solution(survey, choices):
    scoreMap = [0, 3, 2, 1, 0, 1, 2, 3]
    types = dict.fromkeys(["R","T","C","F","J","M","A","N"], 0)
    
    for s, c in zip(survey, choices) :
        disagree, agree = s
        if c >= 4 :
            types[agree] += scoreMap[c]
        elif c < 4 :
            types[disagree] += scoreMap[c]
        
    answer = ""
    for a, b in ["RT", "CF", "JM", "AN"] :
        if types[a] >= types[b] :
            answer += a
        else :
            answer += b
    
    return answer
        