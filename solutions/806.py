class Solution(object):
    def numTilings(self, n):
        mod = 10**9 + 7
        dp = [0] * (n+3)
        dp[0], dp[1], dp[2] = 1, 1, 2
        
        for i in range(3, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % mod
        
        return dp[n]
