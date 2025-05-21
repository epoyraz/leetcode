class Solution(object):
    def minReorder(self, n, connections):
        from collections import deque
        # Build adjacency: (neighbor, needs_reorder)
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append((v, 1))  # edge u->v needs reorder when going from u to v
            adj[v].append((u, 0))  # edge v->u is originally u->v, so no reorder
        
        count = 0
        visited = [False] * n
        dq = deque([0])
        visited[0] = True
        
        while dq:
            u = dq.popleft()
            for v, need in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    count += need
                    dq.append(v)
        
        return count
