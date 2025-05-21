class Solution:
    def maximalNetworkRank(self, n, roads):
        # Count degrees and record direct connections
        degree = [0] * n
        connected = [[False]*n for _ in range(n)]
        
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected[a][b] = True
            connected[b][a] = True
        
        # Compute the max network rank over all pairs
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                # sum of degrees minus 1 if there's a direct road between them
                rank = degree[i] + degree[j] - (1 if connected[i][j] else 0)
                if rank > max_rank:
                    max_rank = rank
        
        return max_rank
