MOD = 10**9 + 7

class Solution:
    def numOfArrays(self, n, m, k):
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        
        for j in range(1, m + 1):
            dp[1][j][1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for x in range(1, k + 1):
                    dp[i][j][x] = dp[i - 1][j][x] * j % MOD
                    for p in range(1, j):
                        dp[i][j][x] = (dp[i][j][x] + dp[i - 1][p][x - 1]) % MOD

        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD
