from collections import defaultdict
from bisect import bisect_right

class Solution:
    def countPairs(self, n, edges, queries):
        deg = [0] * (n + 1)
        freq = defaultdict(int)

        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            freq[(u, v)] += 1

        sorted_deg = sorted(deg[1:])
        res = []

        for q in queries:
            count = 0
            l, r = 0, n - 1

            # Two-pointer approach to count pairs (i, j) with deg[i] + deg[j] > q
            while l < r:
                if sorted_deg[l] + sorted_deg[r] <= q:
                    l += 1
                else:
                    count += r - l
                    r -= 1

            # Subtract overcounted pairs where shared edge count makes sum <= q
            for (u, v), shared in freq.items():
                if deg[u] + deg[v] > q and deg[u] + deg[v] - shared <= q:
                    count -= 1

            res.append(count)

        return res
