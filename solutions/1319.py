from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = Counter(arr).values()
        return len(freq) == len(set(freq))
