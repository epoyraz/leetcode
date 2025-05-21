class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        n = len(arr1)
        res = 0

        for p, q in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            min_val = float('inf')
            max_val = float('-inf')

            for i in range(n):
                val = p * arr1[i] + q * arr2[i] + i
                min_val = min(min_val, val)
                max_val = max(max_val, val)

            res = max(res, max_val - min_val)

        return res
