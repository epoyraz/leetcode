class Solution(object):
    def minOperationsQueries(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(1000000)
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        LOG = (n-1).bit_length()
        parent = [[-1]*n for _ in range(LOG)]
        depth = [0]*n
        
        # cnt[u][w] = number of edges of weight w on path from root to u
        # weights are 1..26, we'll zero-index them 0..25
        cnt = [[0]*26 for _ in range(n)]
        
        # DFS to set depth, parent[0], and cnt
        def dfs(u, p):
            for v, w in adj[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                parent[0][v] = u
                # inherit counts from u
                cnt[v] = cnt[u][:]  # copy list
                cnt[v][w-1] += 1
                dfs(v, u)
        
        # root the tree at 0
        dfs(0, -1)
        
        # Build binary lifting table
        for k in range(1, LOG):
            for v in range(n):
                pv = parent[k-1][v]
                parent[k][v] = parent[k-1][pv] if pv != -1 else -1
        
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # lift u up to depth[v]
            diff = depth[u] - depth[v]
            b = 0
            while diff:
                if diff & 1:
                    u = parent[b][u]
                diff >>= 1
                b += 1
            if u == v:
                return u
            # lift both
            for k in range(LOG-1, -1, -1):
                pu = parent[k][u]
                pv = parent[k][v]
                if pu != pv:
                    u = pu
                    v = pv
            return parent[0][u]
        
        res = []
        for a, b in queries:
            c = lca(a, b)
            # path length in edges
            d = depth[a] + depth[b] - 2*depth[c]
            # find maximum frequency of any weight on the path
            maxf = 0
            for w in range(26):
                f = cnt[a][w] + cnt[b][w] - 2*cnt[c][w]
                if f > maxf:
                    maxf = f
            # minimum ops = path length - most common weight count
            res.append(d - maxf)
        return res
