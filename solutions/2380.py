import bisect

class BookMyShow:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        # each row i has a list of free intervals [[l0,r0],[l1,r1],...]
        self.free = [[[0, m-1]] for _ in range(n)]
        # segment tree arrays
        size = 1
        while size < n: size <<= 1
        self.size = size
        # sum of free seats in segment
        self.segSum = [0] * (2*size)
        # max free-interval length in segment
        self.segMax = [0] * (2*size)
        
        # initialize leaves
        for i in range(n):
            length = m  # one interval [0,m-1]
            p = size + i
            self.segSum[p] = length
            self.segMax[p] = length
        # build internal nodes
        for p in range(size-1, 0, -1):
            self.segSum[p] = self.segSum[2*p] + self.segSum[2*p+1]
            self.segMax[p] = max(self.segMax[2*p], self.segMax[2*p+1])
    
    def _update_row(self, row):
        """Recompute segSum and segMax at leaf row and push up."""
        p = self.size + row
        total = 0
        mx = 0
        for l,r in self.free[row]:
            length = r - l + 1
            total += length
            if length > mx:
                mx = length
        self.segSum[p] = total
        self.segMax[p] = mx
        p //= 2
        while p:
            self.segSum[p] = self.segSum[2*p] + self.segSum[2*p+1]
            self.segMax[p] = max(self.segMax[2*p], self.segMax[2*p+1])
            p //= 2
    
    def _query_sum(self, row_lo, row_hi):
        """Sum of free seats in [row_lo..row_hi]."""
        lo = row_lo + self.size
        hi = row_hi + self.size
        s = 0
        while lo <= hi:
            if lo & 1:
                s += self.segSum[lo]
                lo += 1
            if not (hi & 1):
                s += self.segSum[hi]
                hi -= 1
            lo //= 2
            hi //= 2
        return s
    
    def _find_first_max(self, k, row_lo, row_hi):
        """
        Find the smallest row index in [row_lo..row_hi]
        whose segMax >= k. Return -1 if none.
        """
        def dfs(p, start, end):
            if start > row_hi or end < row_lo or self.segMax[p] < k:
                return -1
            if start == end:
                return start
            mid = (start + end)//2
            res = dfs(2*p, start, mid)
            if res != -1:
                return res
            return dfs(2*p+1, mid+1, end)
        
        return dfs(1, 0, self.size-1)
    
    def _find_first_sum(self, row_lo, row_hi):
        """
        Find smallest row in [row_lo..row_hi] with segSum >= 1.
        """
        def dfs(p, start, end):
            if start > row_hi or end < row_lo or self.segSum[p] < 1:
                return -1
            if start == end:
                return start
            mid = (start + end)//2
            res = dfs(2*p, start, mid)
            if res != -1:
                return res
            return dfs(2*p+1, mid+1, end)
        
        return dfs(1, 0, self.size-1)
    
    def gather(self, k, maxRow):
        # find row with a free interval of length >= k
        row = self._find_first_max(k, 0, maxRow)
        if row == -1:
            return []
        # in that row, find the first interval with length >= k
        intervals = self.free[row]
        for idx, (l, r) in enumerate(intervals):
            length = r - l + 1
            if length >= k:
                start_seat = l
                # allocate [l, l+k-1]
                if length == k:
                    intervals.pop(idx)
                else:
                    intervals[idx][0] += k
                break
        
        # update segment tree for this row
        self._update_row(row)
        return [row, start_seat]
    
    def scatter(self, k, maxRow):
        # check total seats available
        available = self._query_sum(0, maxRow)
        if available < k:
            return False
        
        # allocate k seats greedily
        while k > 0:
            row = self._find_first_sum(0, maxRow)
            # there's guaranteed to be one
            intervals = self.free[row]
            l, r = intervals[0]
            length = r - l + 1
            take = min(length, k)
            # allocate [l, l+take-1]
            if length == take:
                intervals.pop(0)
            else:
                intervals[0][0] += take
            k -= take
            self._update_row(row)
        
        return True
