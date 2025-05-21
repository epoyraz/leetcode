from collections import deque

class Solution(object):
    def minScore(self, n, roads):
        # build adjacency list
        adj = [[] for _ in range(n+1)]
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))
        # BFS/DFS from city 1 to collect all edges in its component
        visited = [False] * (n+1)
        q = deque([1])
        visited[1] = True
        min_edge = float('inf')
        while q:
            u = q.popleft()
            for v, d in adj[u]:
                # track the smallest edge seen in this component
                if d < min_edge:
                    min_edge = d
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return min_edge
