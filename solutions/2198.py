class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.r[rx] < self.r[ry]:
            self.p[rx] = ry
        elif self.r[ry] < self.r[rx]:
            self.p[ry] = rx
        else:
            self.p[ry] = rx
            self.r[rx] += 1
        return True

class Solution:
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        dsu = DSU(n)
        res = []
        
        for u, v in requests:
            ru, rv = dsu.find(u), dsu.find(v)
            # if already in same group, it's successful
            if ru == rv:
                res.append(True)
                continue
            
            # check all restrictions: merging ru and rv should not put any
            # restricted pair into same component
            ok = True
            for x, y in restrictions:
                rx, ry = dsu.find(x), dsu.find(y)
                # after merge, ru and rv become same. So if one of {rx,ry}
                # equals ru and the other equals rv, they'd be together
                if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                    ok = False
                    break
            
            if ok:
                dsu.union(ru, rv)
                res.append(True)
            else:
                res.append(False)
        
        return res
