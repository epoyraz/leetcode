class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # BIT for alive counts
        size = n
        bit = [0] * (size + 1)
        def bit_add(i, v):
            # i: 0-based index
            x = i + 1
            while x <= size:
                bit[x] += v
                x += x & -x
        def bit_sum(i):
            # sum [0..i]
            s = 0
            x = i + 1
            while x > 0:
                s += bit[x]
                x -= x & -x
            return s
        def range_sum(l, r):
            if l > r: return 0
            return bit_sum(r) - (bit_sum(l-1) if l>0 else 0)

        # initialize all alive
        for i in range(n): bit_add(i, 1)
        # sort values with original indices
        arr = sorted((v, i) for i, v in enumerate(nums))
        ops = 0
        cur = 0  # current front pointer in original indices
        for _, idx in arr:
            if idx >= cur:
                steps = range_sum(cur, idx-1)
            else:
                steps = range_sum(cur, n-1) + range_sum(0, idx-1)
            ops += steps + 1  # rotations + removal
            # remove idx
            bit_add(idx, -1)
            cur = idx
            # advance cur to next alive
            # but removal makes next front at same idx position
        return ops
