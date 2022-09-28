def solution(name):
    counts = []
    
    for c in name :
        counts.append(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1))

    minCnt = len(counts)-1
    for i in range(len(counts)) :
        left = right = i
        while left >= 0 and counts[left] == 0 :
            left -= 1
        while right < len(counts) and counts[right] == 0 :
            right += 1
        if left == right : 
            continue
        if 0 <= left and right < len(counts) :
            minCnt = min(minCnt, min(left + (len(counts) - right) * 2, left * 2 + (len(counts) - right)))
        elif left < 0 and right < len(counts) :
            minCnt = min(minCnt, len(counts) - right)
        elif right >= len(counts) and left >= 0 :
            minCnt = min(minCnt, left)
        else :
            minCnt = 0
    
    return sum(counts) + minCnt