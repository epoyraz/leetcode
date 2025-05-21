class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(n, k):
            if n == 1:
                return '0'
            length = (1 << n) - 1  # Length of Sn = 2^n - 1
            mid = length // 2 + 1
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                mirror = mid - (k - mid)
                return '1' if helper(n - 1, mirror) == '0' else '0'

        return helper(n, k)
