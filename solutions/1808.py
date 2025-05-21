class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        # prefix sums: presum[i] = sum of stones[0..i-1]
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i+1] = presum[i] + stones[i]

        # helper to get sum of stones[i..j], inclusive
        def range_sum(i, j):
            return presum[j+1] - presum[i]

        # dp[i][j]: max score difference current player can achieve on stones[i..j]
        dp = [[0] * n for _ in range(n)]

        # length = 2 to n
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                # if remove stones[i], gain = sum(i+1..j), then opponent plays (i+1,j)
                score_remove_i = range_sum(i+1, j) - dp[i+1][j]
                # if remove stones[j], gain = sum(i..j-1), then opponent plays (i,j-1)
                score_remove_j = range_sum(i, j-1) - dp[i][j-1]
                dp[i][j] = max(score_remove_i, score_remove_j)

        return dp[0][n-1]
