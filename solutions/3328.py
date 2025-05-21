import math

class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        min_ops = float('inf')

        for x in range(1, k + 1):
            # Number of duplicates needed to reach at least k with value x
            c = (k + x - 1) // x - 1  # ceil(k / x) - 1
            ops = (x - 1) + c
            min_ops = min(min_ops, ops)

        return min_ops
