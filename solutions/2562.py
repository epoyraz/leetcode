class Solution:
    def countGoodStrings(self, low, high, zero, one):
        MOD = 10**9 + 7
        # dp[i] = number of ways to build a string of length exactly i
        dp = [0] * (high + 1)
        dp[0] = 1

        for length in range(1, high + 1):
            total = 0
            if length >= zero:
                total += dp[length - zero]
            if length >= one:
                total += dp[length - one]
            dp[length] = total % MOD

        # sum counts for all lengths in [low..high]
        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % MOD

        return result
