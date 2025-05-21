MOD = 10**9 + 7

class Solution:
    def countHousePlacements(self, n):
        a, b = 1, 2  # dp[0], dp[1]
        for _ in range(2, n + 1):
            a, b = b, (a + b) % MOD
        return (b * b) % MOD
