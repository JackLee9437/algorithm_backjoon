def solution(words):
    trie = {"count": 0, "children": {}}
    for word in words :
        trie["count"] += 1
        cur = trie["children"]
        for c in word :
            if c not in cur :
                cur[c] = {"count": 0, "children": {}}
            cur[c]["count"] += 1
            cur = cur[c]["children"]
    
    answer = 0
    
    for word in words :
        cur = trie
        for c in word :
            if cur["count"] == 1 :
                break
            answer += 1
            cur = cur["children"][c]
            
    return answer