from collections import deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS from source
        seen = [False] * n
        q = deque([source])
        seen[source] = True
        
        while q:
            u = q.popleft()
            if u == destination:
                return True
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
        return False
