from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                res += count
                dp[i][diff] += count + 1
        
        return res
