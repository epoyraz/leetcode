class Solution(object):
    class BIT:
        # 0-indexed BIT supporting point updates and prefix sums
        def __init__(self, n):
            self.n = n
            self.fw = [0] * (n + 1)
        def update(self, i, delta):
            # add delta at index i
            i += 1
            while i <= self.n:
                self.fw[i] += delta
                i += i & -i
        def query(self, i):
            # sum from 0..i
            i += 1
            s = 0
            while i > 0:
                s += self.fw[i]
                i -= i & -i
            return s
        def range_sum(self, l, r):
            if l > r:
                return 0
            return self.query(r) - (self.query(l - 1) if l > 0 else 0)
    
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Map each value to its list of positions
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)
        
        # Sort distinct values
        vals = sorted(pos.keys())
        
        bit = Solution.BIT(n)
        # Initially block all zeros
        if 0 in pos:
            for idx in pos[0]:
                bit.update(idx, 1)
        
        ans = 0
        # Process positive values in increasing order
        for v in vals:
            if v == 0:
                continue
            idxs = pos[v]
            prev = None
            for idx in idxs:
                if prev is None:
                    ans += 1
                else:
                    # if there's any blocked (i.e. smaller) index between prev and idx
                    if bit.range_sum(prev + 1, idx - 1) > 0:
                        ans += 1
                prev = idx
            # now mark these positions as blocked for future larger values
            for idx in idxs:
                bit.update(idx, 1)
        
        return ans
