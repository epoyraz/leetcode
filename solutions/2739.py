from collections import defaultdict

class Solution(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # Helper to find path and increment freq
        freq = [0]*n
        def dfs_path(src, dst):
            # return path list from src to dst
            stack = [(src, -1)]
            parent = {src: None}
            while stack:
                u, p = stack.pop()
                if u==dst: break
                for v in adj[u]:
                    if v==p: continue
                    if v not in parent:
                        parent[v]=u
                        stack.append((v,u))
            # reconstruct path
            path = []
            cur = dst
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return path
        # accumulate frequencies
        for s,t in trips:
            path = dfs_path(s,t)
            for u in path:
                freq[u]+=1
        # base cost
        base = sum(freq[i]*price[i] for i in range(n))
        # compute savings weights
        weight = [freq[i]*price[i]//2 for i in range(n)]
        # DP on tree for maximum savings
        # root at 0
        seen = [False]*n
        def dfs(u):
            seen[u]=True
            take = weight[u]  # if we take u
            notake = 0        # if we don't take u
            for v in adj[u]:
                if seen[v]: continue
                t_v, nt_v = dfs(v)
                # if u taken, children cannot be taken
                take += nt_v
                # if u not taken, children may be taken or not
                notake += max(t_v, nt_v)
            return take, notake
        max_save, no_save = dfs(0)
        best_save = max(max_save, no_save)
        return base - best_save