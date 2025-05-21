class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        Q = len(queries)
        # Precompute, for each position i, a list of (query_index, value)
        # for queries that cover i.
        cover = [[] for _ in range(n)]
        for qi, (l, r, v) in enumerate(queries):
            for i in range(l, r+1):
                cover[i].append((qi, v))
        # Helper: can we zero out all nums using only queries [0..k-1]?
        def can(k):
            for i in range(n):
                target = nums[i]
                if target == 0:
                    continue
                # dp bitset: bit s is 1 if sum s reachable
                dp = 1
                for qi, v in cover[i]:
                    if qi >= k:
                        break
                    dp |= (dp << v)
                    # early exit if we've hit the target
                    if (dp >> target) & 1:
                        break
                # if target sum not reachable, fail
                if ((dp >> target) & 1) == 0:
                    return False
            return True

        # Check if 0 queries suffice
        if can(0):
            return 0
        # Binary search least k in [1..Q] with can(k)=True
        lo, hi, ans = 1, Q, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
