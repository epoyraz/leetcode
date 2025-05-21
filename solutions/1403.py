class Solution:
    def palindromePartition(self, s, k):
        n = len(s)

        # Precompute the cost to make s[i:j+1] a palindrome
        cost = [[0] * n for _ in range(n)]
        for l in range(n):
            for i in range(n - l):
                j = i + l
                if i >= j:
                    cost[i][j] = 0
                else:
                    cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        # DP: dp[i][k] = min cost to split first i characters into k palindromic parts
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for p in range(1, k + 1):
                for j in range(p - 1, i):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])

        return dp[n][k]
