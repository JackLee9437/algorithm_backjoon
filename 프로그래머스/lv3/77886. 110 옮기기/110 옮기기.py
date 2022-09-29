def solution(s):
    answer = []
    for binary in s :
        stk = []
        removed = 0
        for b in binary :
            if b == "1" :
                stk.append(b)
                continue
            if len(stk) > 1 and stk[-2]=="1" and stk[-1]=="1" :
                for _ in range(2) :
                    stk.pop()
                removed += 1
            else :
                stk.append(b)
        zeroPos = 0
        for zeroPos in range(len(stk)-1,-1,-1) :
            if stk[zeroPos] == "0" :
                break
        else :
            zeroPos -= 1
        stk.insert(zeroPos+1, "110"*removed)
        answer.append(''.join(stk))

    return answer