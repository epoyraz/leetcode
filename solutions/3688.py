class Solution(object):
    def maxSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:                         # cannot delete the only element
            return nums[0]

        INF = 10 ** 18

        # --------  segment tree  ------------------------------------------
        size = 1
        while size < n:
            size <<= 1                    # power of two â¥ n

        total  = [0]           * (2 * size)
        prefix = [-INF]        * (2 * size)
        suffix = [-INF]        * (2 * size)
        best   = [-INF]        * (2 * size)

        # leaves
        for i, v in enumerate(nums):
            idx = size + i
            total[idx] = prefix[idx] = suffix[idx] = best[idx] = v
        # internal nodes
        for i in range(size - 1, 0, -1):
            l, r = i * 2, i * 2 + 1
            total[i]  = total[l] + total[r]
            prefix[i] = max(prefix[l], total[l] + prefix[r])
            suffix[i] = max(suffix[r], total[r] + suffix[l])
            best[i]   = max(best[l], best[r], suffix[l] + prefix[r])

        def combine(a, b):
            """combine two 4-tuples"""
            if a is None:
                return b
            if b is None:
                return a
            at, ap, asu, ab = a
            bt, bp, bs, bb = b
            nt  = at + bt
            np  = max(ap, at + bp)
            ns  = max(bs, bt + asu)
            nb  = max(ab, bb, asu + bp)
            return (nt, np, ns, nb)

        def query(l, r):
            """inclusive range query"""
            l += size
            r += size + 1
            left = right = None
            while l < r:
                if l & 1:
                    left  = combine(left,
                                     (total[l], prefix[l], suffix[l], best[l]))
                    l += 1
                if r & 1:
                    r -= 1
                    right = combine((total[r], prefix[r], suffix[r], best[r]),
                                     right)
                l //= 2
                r //= 2
            return combine(left, right)

        # -------------------------------------------------------------------
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        answer = best[1]                  # no-deletion answer

        for v, idxs in pos.items():
            if len(idxs) == n:            # removing v empties the array
                continue
            prev = 0
            agg = None
            for p in idxs:
                if prev <= p - 1:         # segment before this v
                    agg = combine(agg, query(prev, p - 1))
                prev = p + 1
            if prev <= n - 1:             # tail segment
                agg = combine(agg, query(prev, n - 1))
            answer = max(answer, agg[3])  # agg[3] == best subarray

        return answer
