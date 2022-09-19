def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    mapping = {x : i for i, x in enumerate(enroll)}
    graph = [0] * len(enroll)
    for i in range(len(referral)) :
        if referral[i] == "-" :
            graph[i] = -1
        else :
            graph[i] = mapping[referral[i]]
    
    for s, a in zip(seller, amount) :
        a *= 100
        answer[mapping[s]] += a * 9 // 10
        a //= 10
        s = graph[mapping[s]]
        while s != -1 :
            if a < 10 :
                answer[s] += a
                break
            else :
                tmp = a - a // 10
                answer[s] += tmp
                a -= tmp
                s = graph[s]
    
    return answer
                