class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        
        def is_strictly_increasing(start):
            for i in range(start + 1, start + k):
                if nums[i] <= nums[i - 1]:
                    return False
            return True
        
        for i in range(n - 2 * k + 1):
            if is_strictly_increasing(i) and is_strictly_increasing(i + k):
                return True
        
        return False
