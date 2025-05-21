class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Build a dictionary to store the index of each character in s
        pos_s = {ch: i for i, ch in enumerate(s)}
        res = 0

        # Go through each character in t and compute the difference in index
        for i, ch in enumerate(t):
            res += abs(pos_s[ch] - i)

        return res
