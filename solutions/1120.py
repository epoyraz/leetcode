class Solution:
    def gardenNoAdj(self, n, paths):
        g = [[] for _ in range(n)]
        for u, v in paths:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        ans = [0] * n
        for i in range(n):
            used = {ans[v] for v in g[i]}
            for c in (1, 2, 3, 4):
                if c not in used:
                    ans[i] = c
                    break
        return ans
