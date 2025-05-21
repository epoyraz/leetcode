class Solution:
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        dp = [1] * m

        for j in range(m):
            for i in range(j):
                if all(strs[row][i] <= strs[row][j] for row in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)

        return m - max(dp)
