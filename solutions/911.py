class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]
        dp[0][0][0] = 1

        for i in range(1, len(group) + 1):
            g = group[i - 1]
            p = profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= g:
                        dp[i][j][k] += dp[i - 1][j - g][max(0, k - p)]
                        dp[i][j][k] %= MOD

        return sum(dp[len(group)][j][minProfit] for j in range(n + 1)) % MOD
