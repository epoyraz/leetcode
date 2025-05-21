class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        res = f
        
        for i in range(n - 1, 0, -1):
            f = f + total_sum - n * nums[i]
            res = max(res, f)
        
        return res
