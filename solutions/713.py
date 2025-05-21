class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        
        prod = 1
        result = 0
        left = 0
        
        for right, value in enumerate(nums):
            prod *= value
            while prod >= k:
                prod //= nums[left]
                left += 1
            # All subarrays ending at 'right' with start in [left..right]
            result += right - left + 1
        
        return result
