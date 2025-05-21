class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, c in enumerate(s, 1):
            rev_idx = 26 - (ord(c) - ord('a'))
            total += rev_idx * i
        return total
