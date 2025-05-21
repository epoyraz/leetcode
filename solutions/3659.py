class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][x] = #paths to (i,j) whose XOR-sum is x
        dp = [[[0]*16 for _ in range(n)] for _ in range(m)]
        dp[0][0][ grid[0][0] ] = 1
        
        for i in range(m):
            for j in range(n):
                # propagate from (i,j) to right/down
                for x in range(16):
                    cnt = dp[i][j][x]
                    if not cnt:
                        continue
                    # move right
                    if j+1 < n:
                        nx = x ^ grid[i][j+1]
                        dp[i][j+1][nx] = (dp[i][j+1][nx] + cnt) % MOD
                    # move down
                    if i+1 < m:
                        nx = x ^ grid[i+1][j]
                        dp[i+1][j][nx] = (dp[i+1][j][nx] + cnt) % MOD
        
        return dp[m-1][n-1][k] % MOD
