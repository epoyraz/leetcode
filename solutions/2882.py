class Solution:
    def numberOfWays(self, n, x):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        
        num = 1
        while num**x <= n:
            power = num**x
            for i in range(n, power - 1, -1):
                dp[i] = (dp[i] + dp[i - power]) % MOD
            num += 1
        
        return dp[n]
