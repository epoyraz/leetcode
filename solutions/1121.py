class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [0] * (n + 1)          # dp[i] = max sum for first i elements
        for i in range(1, n + 1):
            cur_max = 0
            for l in range(1, min(k, i) + 1):   # partition length l ending at i-1
                cur_max = max(cur_max, arr[i - l])
                dp[i] = max(dp[i], dp[i - l] + cur_max * l)
        return dp[n]
