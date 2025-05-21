class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        # build segment tree for rangeâmax
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2*size)
        for i, h in enumerate(heights):
            seg[size+i] = h
        for i in range(size-1, 0, -1):
            seg[i] = max(seg[2*i], seg[2*i+1])

        # find first index >= L with heights[idx] > H
        def find_first_greater(L, H, node, lo, hi):
            if hi < L or seg[node] <= H:
                return -1
            if lo == hi:
                return lo
            mid = (lo + hi) // 2
            res = find_first_greater(L, H, 2*node, lo, mid)
            if res != -1:
                return res
            return find_first_greater(L, H, 2*node+1, mid+1, hi)

        ans = []
        for a, b in queries:
            if a == b:
                ans.append(a)
                continue

            ha, hb = heights[a], heights[b]
            candidates = []

            # Bob moves to Alice?
            if a > b and ha > hb:
                candidates.append(a)
            # Alice moves to Bob?
            if b > a and hb > ha:
                candidates.append(b)

            # both must move forward
            L = max(a, b) + 1
            if L < n:
                k = find_first_greater(L, max(ha, hb), 1, 0, size-1)
                if 0 <= k < n:
                    candidates.append(k)

            ans.append(min(candidates) if candidates else -1)

        return ans