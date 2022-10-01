from collections import deque

class Trie :
    def __init__(self) :
        self.children = {}
        self.val = None

def solution(strs, t):
    trie = Trie()
    for s in strs :
        now = trie
        for c in s :
            if c not in now.children :
                now.children[c] = Trie()
            now = now.children[c]
        now.val = s
    
    visited = [0] * (len(t)+1)
    visited[0] = 1
    que = deque([(0, 0)])
    while que :
        cur, cnt = que.popleft()
        if cur == len(t) :
            return cnt
        now = trie
        for _ in range(5) :
            if cur == len(t) or t[cur] not in now.children :
                break
            now = now.children[t[cur]]
            if now.val and not visited[cur+1]:
                visited[cur+1] = 1
                que.append((cur+1, cnt+1))
            cur += 1
    return -1
            
        
        