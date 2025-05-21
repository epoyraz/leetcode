class Solution:
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # Ensure n <= m by transposing if needed (to minimize DP width)
        if n > m:
            # Transpose grid
            grid = list(map(list, zip(*grid)))
            m, n = n, m

        # dp[j][r]: number of ways to reach column j in current row with sum mod k == r
        dp = [ [0]*k for _ in range(n) ]

        for i in range(m):
            new_dp = [ [0]*k for _ in range(n) ]
            for j in range(n):
                val = grid[i][j] % k
                if i == 0 and j == 0:
                    # start cell
                    new_dp[0][val] = 1
                else:
                    # from top (previous row, same col)
                    if i > 0:
                        for r in range(k):
                            cnt = dp[j][r]
                            if cnt:
                                new_dp[j][(r + val) % k] = (new_dp[j][(r + val) % k] + cnt) % MOD
                    # from left (current row, col-1)
                    if j > 0:
                        left = new_dp[j-1]
                        for r in range(k):
                            cnt = left[r]
                            if cnt:
                                new_dp[j][(r + val) % k] = (new_dp[j][(r + val) % k] + cnt) % MOD
            dp = new_dp

        # answer at bottom-right cell, sum mod k == 0
        return dp[n-1][0]
