class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Sort edges by weight ascending
        edgeList.sort(key=lambda x: x[2])
        # Augment queries with original indices and sort by limit ascending
        queries_with_idx = [
            (limit, u, v, i)
            for i, (u, v, limit) in enumerate(queries)
        ]
        queries_with_idx.sort(key=lambda x: x[0])

        dsu = DSU(n)
        res = [False] * len(queries)
        ei = 0  # pointer into edgeList

        # Process each query in order of increasing limit
        for limit, u, v, qi in queries_with_idx:
            # Union all edges with weight < limit
            while ei < len(edgeList) and edgeList[ei][2] < limit:
                a, b, w = edgeList[ei]
                dsu.union(a, b)
                ei += 1
            # After adding those edges, u and v are connected iff a valid path exists
            res[qi] = (dsu.find(u) == dsu.find(v))

        return res
