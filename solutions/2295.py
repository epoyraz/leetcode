import math

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        MAX_LAPS = 20  # Reasonable limit since time grows exponentially per tire
        INF = float('inf')

        # Precompute minimal time for doing i laps without tire change
        min_time_for_laps = [INF] * (MAX_LAPS + 1)
        for f, r in tires:
            total = 0
            cur = f
            for i in range(1, MAX_LAPS + 1):
                total += cur
                if total > 10**7:
                    break
                min_time_for_laps[i] = min(min_time_for_laps[i], total)
                cur *= r

        # DP to compute minimal total time for numLaps
        dp = [INF] * (numLaps + 1)
        dp[0] = 0
        for i in range(1, numLaps + 1):
            for j in range(1, min(i, MAX_LAPS) + 1):
                if i == j:
                    dp[i] = min(dp[i], min_time_for_laps[j])
                else:
                    dp[i] = min(dp[i], dp[i - j] + changeTime + min_time_for_laps[j])
        return dp[numLaps]
