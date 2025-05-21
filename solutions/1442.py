from collections import defaultdict, deque

class Solution:
    def makeConnected(self, n, connections):
        # Need at least n-1 cables to connect n computers
        if len(connections) < n - 1:
            return -1
        
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        components = 0
        
        # Count connected components with BFS
        for i in range(n):
            if not visited[i]:
                components += 1
                queue = deque([i])
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    for nei in adj[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            queue.append(nei)
        
        # To connect k components, need k-1 extra cables
        return components - 1
