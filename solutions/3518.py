class Solution(object):
    def maxScore(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        dp = [float('-inf')] * 5  # dp[i] = max score using i elements
        dp[0] = 0  # base case: using 0 elements gives 0 score

        for val in b:
            # iterate in reverse to avoid overwriting previous states
            for i in range(3, -1, -1):
                dp[i+1] = max(dp[i+1], dp[i] + a[i] * val)

        return dp[4]
