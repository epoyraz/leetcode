class Solution:
    def maxScore(self, nums, x):
        n = len(nums)
        even = odd = float('-inf')
        if nums[0] % 2 == 0:
            even = nums[0]
        else:
            odd = nums[0]
        
        for i in range(1, n):
            val = nums[i]
            if val % 2 == 0:
                even = max(even + val, odd + val - x)
            else:
                odd = max(odd + val, even + val - x)
        
        return max(even, odd)
