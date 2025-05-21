class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            max_score = float('-inf')
            total = 0
            for k in range(1, 4):
                if i + k <= n:
                    total += stoneValue[i + k - 1]
                    max_score = max(max_score, total - dp[i + k])
            dp[i] = max_score

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
