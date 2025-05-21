class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(num for i, num in enumerate(nums) if bin(i).count('1') == k)
