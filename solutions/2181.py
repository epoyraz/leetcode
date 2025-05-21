class Solution:
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, v in enumerate(nums):
            if i % 10 == v:
                return i
        return -1