class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        
        max_len = max(dp)
        return sum(c for i, c in enumerate(count) if dp[i] == max_len)
