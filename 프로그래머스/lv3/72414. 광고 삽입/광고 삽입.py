def hmsToSec(t) :
    h,m,s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s

def secToHms(sec) :
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d"%(h,m,s)

def solution(play_time, adv_time, logs):
    pt = hmsToSec(play_time)
    at = hmsToSec(adv_time)
    
    logsStart = []
    logsEnd = []
    for log in logs :
        start, end = log.split("-")
        logsStart.append(hmsToSec(start))
        logsEnd.append(hmsToSec(end))
    
    totalTime = [0] * (pt + 1)
    for i in range(len(logs)) :
        totalTime[logsStart[i]] += 1
        totalTime[logsEnd[i]] -= 1
    
    for _ in range(2) :
        for i in range(1, pt+1) :
            totalTime[i] += totalTime[i-1]
    
    candiTime = 0
    candiMax = 0
    for t in range(at, pt+1) :
        if (tmp:= totalTime[t] - totalTime[t-at]) > candiMax :
            candiMax = tmp
            candiTime = t-at+1 if totalTime[t] != totalTime[t-1] else t-at
    
    return secToHms(candiTime)