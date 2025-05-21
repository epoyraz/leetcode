class Solution(object):
    def longestIdealString(self, s, k):
        dp = [0] * 26

        for c in s:
            i = ord(c) - ord('a')
            max_len = 0
            for j in range(max(0, i - k), min(26, i + k + 1)):
                max_len = max(max_len, dp[j])
            dp[i] = max(dp[i], max_len + 1)

        return max(dp)
