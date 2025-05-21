class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        
        counts = Counter(nums)
        # If any number occurs more than twice, it's impossible
        return max(counts.values()) <= 2
