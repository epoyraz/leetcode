class Solution(object):
    def minTime(self, n, edges, hasApple):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        def dfs(u, p):
            t = 0
            for v in g[u]:
                if v != p:
                    sub = dfs(v, u)
                    if sub > 0 or hasApple[v]:
                        t += sub + 2
            return t
        return dfs(0, -1)
