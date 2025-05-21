class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        # If fewer jobs than days, impossible
        if n < d:
            return -1
        
        # dp[i][day]: min difficulty to schedule first i jobs in 'day' days
        INF = float('inf')
        dp = [[INF] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        # Fill DP
        for i in range(1, n + 1):
            for day in range(1, min(d, i) + 1):
                max_job = 0
                # Try ending the previous day at k, and day 'day' does jobs k..i-1
                for k in range(i - 1, day - 2, -1):
                    max_job = max(max_job, jobDifficulty[k])
                    prev = dp[k][day - 1]
                    if prev + max_job < dp[i][day]:
                        dp[i][day] = prev + max_job
        
        ans = dp[n][d]
        return ans if ans < INF else -1
