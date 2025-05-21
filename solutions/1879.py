class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        total = a + b + c
        max_pile = max(a, b, c)
        return min(total // 2, total - max_pile)
