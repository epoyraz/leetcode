from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :param values: List[int]         # node values
        :param edges: List[List[int]]    # [u, v, time] undirected
        :param maxTime: int              # time budget
        :return: int                     # maximum quality
        """
        n = len(values)
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        
        visited = [False] * n
        visited[0] = True
        self.max_quality = values[0]
        curr_sum = values[0]
        
        def dfs(u, time_used, curr_sum):
            # If we're back at node 0, consider updating answer
            if u == 0:
                self.max_quality = max(self.max_quality, curr_sum)
            # Try all neighbors
            for v, t in adj[u]:
                new_time = time_used + t
                if new_time > maxTime:
                    continue
                added = 0
                if not visited[v]:
                    visited[v] = True
                    added = values[v]
                    curr_sum += added
                dfs(v, new_time, curr_sum)
                if added:
                    # backtrack
                    visited[v] = False
                    curr_sum -= added
        
        # Start DFS from node 0 at time 0
        dfs(0, 0, curr_sum)
        return self.max_quality
