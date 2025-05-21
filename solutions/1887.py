class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Build adjacency matrix
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        degree = [0] * (n + 1)
        
        for u, v in edges:
            adj[u][v] = True
            adj[v][u] = True
            degree[u] += 1
            degree[v] += 1
        
        min_degree = float('inf')

        # Check all triplets (i, j, k) for being a trio
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if not adj[i][j]:
                    continue
                for k in range(j + 1, n + 1):
                    if adj[i][k] and adj[j][k]:
                        # Trio found
                        trio_deg = degree[i] + degree[j] + degree[k] - 6
                        min_degree = min(min_degree, trio_deg)
        
        return min_degree if min_degree != float('inf') else -1
