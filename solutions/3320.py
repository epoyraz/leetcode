class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        S = nums[0] + nums[1]
        count = 0
        i = 0
        while i + 1 < n and nums[i] + nums[i+1] == S:
            count += 1
            i += 2
        return count
