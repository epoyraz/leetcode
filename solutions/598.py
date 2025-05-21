class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        # The cells with maximum value are those in the intersection
        # of all operation rectangles: [0, min_ai) Ã [0, min_bi)
        min_a = min(a for a, _ in ops)
        min_b = min(b for _, b in ops)
        return min_a * min_b
