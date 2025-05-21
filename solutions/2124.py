class Solution:
    def firstDayBeenInAllRooms(self, nextVisit):
        mod = 10**9 + 7
        n = len(nextVisit)
        dp = [0] * n  # dp[i] = first day we've been in room i

        for i in range(1, n):
            dp[i] = (2 * dp[i-1] - dp[nextVisit[i-1]] + 2) % mod

        return dp[-1]
