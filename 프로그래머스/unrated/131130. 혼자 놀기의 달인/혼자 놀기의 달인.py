def solution(cards):
    cards = [0] + cards
    visited = [0] * len(cards)
    
    cases = []
    for i in range(1, len(cards)) :
        if visited[i] :
            continue
            
        cnt = 1
        j = i
        visited[j] = 1
        chked = set([j])
        while cards[j] not in chked :
            chked.add(cards[j])
            j = cards[j]
            cnt += 1
            visited[j] = 1
        cases.append(cnt)
    
    cases.sort(reverse=True)
    if len(cases) < 2 :
        return 0
    else :
        return cases[0] * cases[1]