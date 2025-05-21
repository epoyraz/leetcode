class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        count = Counter(nums)
        result = 0

        for freq in count.values():
            result += freq * (freq - 1) // 2

        return result
