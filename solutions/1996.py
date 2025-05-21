class Solution:
    def rearrangeSticks(self, n, k):
        mod = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Place the tallest stick at front: dp[i - 1][j - 1]
                # Place the tallest stick somewhere else: (i - 1) * dp[i - 1][j]
                dp[i][j] = (dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]) % mod

        return dp[n][k]
