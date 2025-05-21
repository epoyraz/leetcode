class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        n = len(floor)
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for k in range(numCarpets + 1):
                dp[i][k] = dp[i - 1][k] + (floor[i - 1] == '1')
                if k > 0:
                    cover_start = max(0, i - carpetLen)
                    dp[i][k] = min(dp[i][k], dp[cover_start][k - 1])
        return dp[n][numCarpets]
