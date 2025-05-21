from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        # collect odd and even frequencies
        odd_freqs = [f for f in freq.values() if f % 2 == 1]
        even_freqs = [f for f in freq.values() if f % 2 == 0]

        # problem guarantees at least one odd and one even, but we guard just in case
        if not odd_freqs or not even_freqs:
            return 0

        return max(odd_freqs) - min(even_freqs)
