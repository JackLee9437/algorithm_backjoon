from heapq import heappush, heappop

def solution(jobs):
    jobCount = len(jobs)
    totalTime = 0
    
    jobs.sort()
    sec = 0
    cur = 0
    que = []
    workingJob = None
    completeCnt = 0
    while completeCnt < jobCount :
        while cur < jobCount and jobs[cur][0] == sec :
            heappush(que, (jobs[cur][1], jobs[cur][0]))
            cur += 1
        if not workingJob :
            if que :
                job = heappop(que)
                workingJob = (job[1], sec+job[0])
        else :
            if workingJob[1] == sec :
                totalTime += workingJob[1] - workingJob[0]
                completeCnt += 1
                if que :
                    job = heappop(que)
                    workingJob = (job[1], sec+job[0])
                else :
                    workingJob = None
        sec += 1
    
    answer = totalTime // jobCount
    return answer