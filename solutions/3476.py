class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        for x in nums:
            r = x % 3
            ops += min(r, 3 - r)
        return ops
