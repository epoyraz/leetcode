from collections import Counter

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        return sum(num for num, freq in count.items() if freq == 1)
