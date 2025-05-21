class Fenwick:
    """Fenwick tree for rangeâadd / pointâquery."""
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n+1)
    def _add(self, i, v):
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def range_add(self, l, r, v):
        self._add(l, v)
        self._add(r+1, -v)
    def point_query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

class Solution(object):
    def treeQueries(self, n, edges, queries):
        import sys
        sys.setrecursionlimit(10**7)

        # Build adjacency
        g = [[] for _ in range(n+1)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        tin  = [0] * (n+1)
        tout = [0] * (n+1)
        dist0 = [0] * (n+1)
        edge_weight = {}  # child -> weight to its parent

        timer = [0]  # use list so we can mutate inside dfs

        def dfs(u, p):
            timer[0] += 1
            tin[u] = timer[0]
            for v, w in g[u]:
                if v == p:
                    continue
                dist0[v] = dist0[u] + w
                edge_weight[v] = w
                dfs(v, u)
            tout[u] = timer[0]

        # run DFS from root = 1
        dfs(1, 0)

        bit = Fenwick(n)
        ans = []

        for q in queries:
            if q[0] == 1:
                # Update edge (u,v) to new weight w_new
                _, u, v, w_new = q
                # determine child in our rooted tree by tin/tout
                if tin[u] < tin[v] and tout[v] <= tout[u]:
                    parent, child = u, v
                else:
                    parent, child = v, u
                delta = w_new - edge_weight[child]
                edge_weight[child] = w_new
                bit.range_add(tin[child], tout[child], delta)
            else:
                # Query distance to x
                _, x = q
                d = dist0[x] + bit.point_query(tin[x])
                ans.append(d)

        return ans
