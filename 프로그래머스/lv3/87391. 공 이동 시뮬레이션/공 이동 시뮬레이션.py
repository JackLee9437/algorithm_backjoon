def solution(n, m, x, y, queries):
    rmin = rmax = x
    cmin = cmax = y
    
    def up(dx) :
        nonlocal rmin, rmax, n
        if rmin != 0 :
            rmin = rmin+dx
        rmax = min(n-1, rmax+dx)
        if rmin >= n :
            return False
        return True
    
    def dn(dx) :
        nonlocal rmin, rmax, n
        if rmax != n-1 :
            rmax = rmax-dx
        rmin = max(0, rmin-dx)
        if rmax < 0:
            return False
        return True
    
    def ri(dx) :
        nonlocal cmin, cmax, m
        if cmax != m-1 :
            cmax = cmax-dx
        cmin = max(0, cmin-dx)
        if cmax < 0 :
            return False
        return True
    
    def le(dx) :
        nonlocal cmin, cmax, m
        if cmin != 0 :
            cmin = cmin+dx
        cmax = min(m-1, cmax+dx)
        if cmin >= m :
            return False
        return True
    cmd = [le, ri, up, dn]
    for command, dx in queries[::-1] :
        if not cmd[command](dx) :
            return 0

    return (rmax+1-rmin) * (cmax+1-cmin)
