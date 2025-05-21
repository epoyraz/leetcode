import sys
sys.setrecursionlimit(10**7)

class Solution(object):
    def minimumWeight(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        # build adjacency list
        G = [[] for _ in range(n)]
        for u,v,w in edges:
            G[u].append((v,w))
            G[v].append((u,w))
        
        LOG = (n-1).bit_length()
        up = [[-1]*n for _ in range(LOG)]  # up[k][v] = 2^k-th ancestor of v
        depth = [0]*n
        dist = [0]*n  # distance from root (0)
        
        # iterative DFS to set up depth, parent[0], dist
        stack = [(0, -1, 0, 0)]  # node, parent, depth, dist
        while stack:
            v, p, d, dv = stack.pop()
            up[0][v] = p
            depth[v] = d
            dist[v] = dv
            for w, wt in G[v]:
                if w == p: 
                    continue
                stack.append((w, v, d+1, dv+wt))
        
        # binary-lift preprocessing
        for k in range(1, LOG):
            for v in range(n):
                pv = up[k-1][v]
                up[k][v] = -1 if pv < 0 else up[k-1][pv]
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # lift u up to depth[v]
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1<<k):
                    u = up[k][u]
            if u == v:
                return u
            # binary lift both
            for k in reversed(range(LOG)):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]
        
        def distance(a, b):
            """Return distance between a and b."""
            c = lca(a, b)
            return dist[a] + dist[b] - 2*dist[c]
        
        ans = []
        for u, v, w in queries:
            duw = distance(u, w)
            dvw = distance(v, w)
            duv = distance(u, v)
            # union of paths weight
            ans.append((duw + dvw + duv) // 2)
        
        return ans
