class DSU(object):
    def __init__(self, n):
        self.p = list(range(n+1))
        self.rank = [0] * (n+1)
        self.count = n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.p[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.p[ry] = rx
        else:
            self.p[ry] = rx
            self.rank[rx] += 1
        self.count -= 1
        return True

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        alice = DSU(n)
        bob = DSU(n)
        used = 0

        # use type 3 edges first
        for t, u, v in edges:
            if t == 3 and alice.union(u, v):
                bob.union(u, v)
                used += 1

        # type 1 for Alice
        for t, u, v in edges:
            if t == 1 and alice.union(u, v):
                used += 1

        # type 2 for Bob
        for t, u, v in edges:
            if t == 2 and bob.union(u, v):
                used += 1

        # check fully traversable
        if alice.count != 1 or bob.count != 1:
            return -1
        return len(edges) - used
