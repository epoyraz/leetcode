from collections import Counter

class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        freq = Counter(nums)
        
        best = -10**18
        for s in nums:
            v = total - 2*s
            # check if v exists at some index != the one giving s
            # if v != s, need freq[v] >= 1; if v == s, need freq[v] >= 2
            if v in freq and freq[v] - (1 if v == s else 0) > 0:
                best = max(best, v)
        
        return best
