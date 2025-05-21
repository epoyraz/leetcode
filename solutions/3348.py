class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        # comp_and[x] is valid only when x is a root
        self.comp_and = [~0] * n  # allâones initial mask

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b, w):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            # even if already unioned, we still AND this edge into the component
            self.comp_and[ra] &= w
        else:
            # merge rb into ra
            self.p[rb] = ra
            # the combined component's AND is the AND of both plus this edge
            self.comp_and[ra] = self.comp_and[ra] & self.comp_and[rb] & w

class Solution(object):
    def minimumCost(self, n, edges, query):
        dsu = DSU(n)
        for u, v, w in edges:
            dsu.union(u, v, w)

        ans = []
        for s, t in query:
            rs, rt = dsu.find(s), dsu.find(t)
            if rs != rt:
                ans.append(-1)
            else:
                ans.append(dsu.comp_and[rs])
        return ans
