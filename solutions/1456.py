class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        # Initialize distance matrix
        INF = 10**9
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall to compute all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                # Early skip if no improvement possible
                dik = dist[i][k]
                if dik == INF:
                    continue
                row_i = dist[i]
                row_k = dist[k]
                for j in range(n):
                    nd = dik + row_k[j]
                    if nd < row_i[j]:
                        row_i[j] = nd
        
        # For each city, count reachable within threshold
        best_city = -1
        best_count = n + 1
        for i in range(n):
            count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            # We want the smallest count, and in tie the largest index
            if count < best_count or (count == best_count and i > best_city):
                best_count = count
                best_city = i
        
        return best_city
