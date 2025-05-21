class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        max_len = 0
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            max_len = max(max_len, dp[num])
        return max_len
