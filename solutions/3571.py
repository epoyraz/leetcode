class BIT:
    """Fenwick tree for rangeâmaximum queries on prefix [0..i]."""
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)
    def update(self, i, val):
        # set f[i] = max(f[i], val) and propagate
        i += 1
        while i <= self.n:
            if self.f[i] < val:
                self.f[i] = val
            i += i & -i
    def query(self, i):
        # max over [0..i]
        if i < 0:
            return 0
        i += 1
        res = 0
        while i > 0:
            if self.f[i] > res:
                res = self.f[i]
            i -= i & -i
        return res

class Solution(object):
    def maxPathLength(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(coordinates)
        # attach original indices
        pts = [(coordinates[i][0], coordinates[i][1], i) for i in range(n)]
        # compress y
        ys = sorted({y for _, y, _ in pts})
        y_to_rank = {y: i for i, y in enumerate(ys)}
        M = len(ys)
        # replace y by rank
        pts = [(x, y_to_rank[y], idx) for x, y, idx in pts]

        # dp_before[i] = length of longest increasing chain ending at i
        dp_before = [0] * n
        bit1 = BIT(M)

        # process groups of equal x in ascending x
        pts.sort(key=lambda t: t[0])
        i = 0
        while i < n:
            j = i
            # find range [i..j) with same x
            while j < n and pts[j][0] == pts[i][0]:
                j += 1
            # compute dp for this group without updating bit
            for x, y_r, idx in pts[i:j]:
                best = bit1.query(y_r - 1)
                dp_before[idx] = best + 1
            # now update bit with these dp values
            for x, y_r, idx in pts[i:j]:
                bit1.update(y_r, dp_before[idx])
            i = j

        # dp_after[i] = length of longest increasing chain starting at i
        # i.e., on reversed axes: x desc, y desc
        dp_after = [0] * n
        bit2 = BIT(M)
        # for suffix we invert y-rank: y_rev = (M-1) - y_r
        pts.sort(key=lambda t: t[0], reverse=True)
        i = 0
        while i < n:
            j = i
            while j < n and pts[j][0] == pts[i][0]:
                j += 1
            for x, y_r, idx in pts[i:j]:
                y_rev = (M - 1) - y_r
                best = bit2.query(y_rev - 1)
                dp_after[idx] = best + 1
            for x, y_r, idx in pts[i:j]:
                y_rev = (M - 1) - y_r
                bit2.update(y_rev, dp_after[idx])
            i = j

        # combine: longest through k = dp_before[k] + dp_after[k] - 1
        return dp_before[k] + dp_after[k] - 1
