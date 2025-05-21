class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # If k has a 1-bit where n has 0, impossible
        if k & ~n:
            return -1
        # Otherwise, must clear every 1 in n that's 0 in k
        return bin(n & ~k).count('1')
