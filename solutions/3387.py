class Solution(object):
    def minOperationsToMakeMedianK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        m = n // 2  # index of the âlargerâ median
        ops = 0
        
        # Any tooâlarge values at or before the median must be lowered to k
        for i in range(m+1):
            if nums[i] > k:
                ops += nums[i] - k
        
        # Any tooâsmall values at or after the median must be raised to k
        for i in range(m, n):
            if nums[i] < k:
                ops += k - nums[i]
        
        return ops
