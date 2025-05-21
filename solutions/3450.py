class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # One full back-and-forth takes 2*(n-1) passes
        period = 2 * (n - 1)
        r = k % period
        # If r â¤ n-1, we're moving right from 0; otherwise weâre on the return leg.
        if r <= n - 1:
            return r
        else:
            return period - r
