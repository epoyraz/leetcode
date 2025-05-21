class Solution(object):
    def minSideJumps(self, obstacles):
        n = len(obstacles) - 1
        INF = 10**9
        # dp[l] = min side jumps to be at current point on lane l+1
        dp = [1, 0, 1]
        for i in range(1, n + 1):
            # block lane with obstacle at this point
            b = obstacles[i]
            if b:
                dp[b - 1] = INF
            # for each lane not blocked, consider jumping from the other two lanes
            for l in range(3):
                if obstacles[i] != l + 1:
                    dp[l] = min(dp[l], dp[(l + 1) % 3] + 1, dp[(l + 2) % 3] + 1)
        return min(dp)
