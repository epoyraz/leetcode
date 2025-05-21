import math

class Solution:
    def minSkips(self, dist, speed, hoursBefore):
        n = len(dist)
        INF = float('inf')

        # dp[i][k] = min time (in units) to reach i-th road with k skips
        dp = [ [INF] * (n + 1) for _ in range(n + 1) ]
        dp[0][0] = 0  # 0 roads, 0 skips = 0 time

        for i in range(1, n + 1):
            d = dist[i - 1]
            for k in range(0, i + 1):
                # Option 1: don't skip
                if dp[i - 1][k] != INF:
                    t = dp[i - 1][k] + d
                    if i < n:
                        # round up to next multiple of speed
                        t = ((t + speed - 1) // speed) * speed
                    dp[i][k] = min(dp[i][k], t)

                # Option 2: skip this rest
                if k > 0 and dp[i - 1][k - 1] != INF:
                    t = dp[i - 1][k - 1] + d
                    dp[i][k] = min(dp[i][k], t)

        max_time = hoursBefore * speed
        for k in range(n + 1):
            if dp[n][k] <= max_time:
                return k
        return -1
