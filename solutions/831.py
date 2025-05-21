class Solution(object):
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = prefix[i] * 1.0 / i
        
        for _ in range(k-1):
            for i in range(n, 0, -1):
                for j in range(i):
                    dp[i] = max(dp[i], dp[j] + (prefix[i] - prefix[j]) * 1.0 / (i-j))
        
        return dp[n]
