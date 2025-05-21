class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        k = s.count(c)
        # Number of ways to choose start and end among k occurrences,
        # allowing start == end: k * (k + 1) / 2
        return k * (k + 1) // 2
