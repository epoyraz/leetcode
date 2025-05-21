class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, skip = questions[i]
            next_q = i + skip + 1
            dp[i] = max(dp[i + 1], points + (dp[next_q] if next_q < n else 0))
        return dp[0]
