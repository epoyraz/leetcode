class Solution:
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        
        _min = min(nums)
        _max = max(nums)
        
        for x in nums:
            if x != _min and x != _max:
                return x
        
        return -1
