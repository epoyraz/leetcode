class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        m = len(queries)

        # If it's already a zero array, zero queries are needed.
        if all(v == 0 for v in nums):
            return 0

        # Helper: can we zero out with the first k queries?
        def can(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l]   += v
                diff[r+1] -= v
            c = 0
            for i in range(n):
                c += diff[i]
                if c < nums[i]:
                    return False
            return True

        # If even all queries can't do it, return -1
        if not can(m):
            return -1

        # Binary search the smallest k in [1..m] for which can(k) is True
        lo, hi = 1, m
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
