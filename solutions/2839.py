class Solution:
    def maximumSumQueries(self, nums1, nums2, queries):
        import bisect
        
        n = len(nums1)
        m = len(queries)
        
        # Collect all nums2 values and all query-yi's for coordinate compression
        ys = set(nums2)
        for x, y in queries:
            ys.add(y)
        # Sort in descending order so that "nums2 >= y" becomes a prefix in this array
        desc = sorted(ys, reverse=True)
        size = len(desc)
        idx_map = {v: i for i, v in enumerate(desc)}
        
        # Fenwick/BIT for range maximum on prefix [0..i]
        NEG = -10**30
        BIT = [NEG] * (size + 1)
        def bit_update(i, val):
            # point update: set BIT[i] = max(BIT[i], val)
            i += 1
            while i <= size:
                if BIT[i] < val:
                    BIT[i] = val
                i += i & -i
        def bit_query(i):
            # prefix max over [0..i]
            i += 1
            res = NEG
            while i > 0:
                if BIT[i] > res:
                    res = BIT[i]
                i -= i & -i
            return res
        
        # Sort points (nums1[j], nums2[j]) by nums1 descending
        pts = sorted(zip(nums1, nums2), key=lambda t: -t[0])
        # Sort queries by xi descending, keep original index
        qs = sorted(((x, y, qi) for qi, (x, y) in enumerate(queries)),
                    key=lambda t: -t[0])
        
        ans = [-1] * m
        p = 0
        
        for x, y, qi in qs:
            # Insert all points with nums1 >= x into the BIT
            while p < n and pts[p][0] >= x:
                a, b = pts[p]
                s = a + b
                bit_update(idx_map[b], s)
                p += 1
            
            # Find the rightmost index pos in 'desc' where desc[pos] >= y
            # i.e., the largest pos with desc[pos] >= y
            lo, hi, pos = 0, size - 1, -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if desc[mid] >= y:
                    pos = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            if pos >= 0:
                res = bit_query(pos)
                if res > NEG // 2:
                    ans[qi] = res
        
        return ans
