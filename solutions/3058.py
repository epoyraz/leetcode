class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        import sys
        sys.setrecursionlimit(10**7)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.count = 0
        def dfs(u, p):
            total = values[u]
            for v in adj[u]:
                if v == p:
                    continue
                subtotal = dfs(v, u)
                if subtotal % k == 0:
                    self.count += 1
                else:
                    total += subtotal
            return total
        dfs(0, -1)
        return self.count + 1