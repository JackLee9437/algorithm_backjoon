def solution(n, build_frame):
    virtualSpace = [[[0,0] for __ in range(n+1)] for _ in range(n+1)]
    built = set()
    
    def isInstallable(r, c, t) :
        nonlocal n
        if t == 0 :
            return r == 0 or (c > 0 and virtualSpace[r][c-1][1]) or virtualSpace[r][c][1] or virtualSpace[r-1][c][0]
        else :
            return virtualSpace[r-1][c][0] or virtualSpace[r-1][c+1][0] or (0 < c < n and virtualSpace[r][c-1][1] and virtualSpace[r][c+1][1])
        
    def isUninstallable(r, c, t) :
        nonlocal n
        virtualSpace[r][c][t] = 0
        if t == 0 :
            if (r < n and virtualSpace[r+1][c][0] and not isInstallable(r+1,c,0)) or (r < n and virtualSpace[r+1][c][1] and not isInstallable(r+1,c,1)) or (r < n and c > 0 and virtualSpace[r+1][c-1][1] and not isInstallable(r+1,c-1,1)) :
                virtualSpace[r][c][t] = 1
                return False
        else :
            if (c > 0 and virtualSpace[r][c-1][1] and not isInstallable(r,c-1,1)) or (c < n and virtualSpace[r][c+1][1] and not isInstallable(r,c+1,1)) or (virtualSpace[r][c][0] and not isInstallable(r,c,0)) or (c < n and virtualSpace[r][c+1][0] and not isInstallable(r,c+1,0)) :
                virtualSpace[r][c][t] = 1
                return False
        virtualSpace[r][c][t] = 1
        return True    
        
    def do(r, c, t, a) :
        if a == 0 :
            if isUninstallable(r, c, t) :
                virtualSpace[r][c][t] = 0
                built.discard((c,r,t))
        else :
            if isInstallable(r, c, t) :
                virtualSpace[r][c][t] = 1
                built.add((c,r,t))
    
    for c, r, t, a in build_frame :
        do(r, c, t, a)
    
    return sorted(built)