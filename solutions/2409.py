class Solution:
    def countPaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j]: number of increasing paths ending at (i, j)
        dp = [[1] * n for _ in range(m)]
        
        # process cells in ascending order of value
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()
        
        for val, i, j in cells:
            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < val:
                    dp[i][j] = (dp[i][j] + dp[ni][nj]) % MOD
        
        # sum all dp[i][j]
        total = 0
        for i in range(m):
            for j in range(n):
                total = (total + dp[i][j]) % MOD
        
        return total
