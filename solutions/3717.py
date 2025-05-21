import heapq
from collections import defaultdict

class SlidingMedian:
    """Maintain median and total absoluteâdeviation cost on a sliding window."""
    def __init__(self):
        self.lo = []       # maxâheap (store negatives)
        self.hi = []       # minâheap
        self.del_lo = defaultdict(int)
        self.del_hi = defaultdict(int)
        self.sz_lo = self.sz_hi = 0
        self.sum_lo = 0
        self.sum_hi = 0

    def _prune(self, heap, to_del):
        while heap and to_del[heap[0]]>0:
            v = heap[0]
            to_del[v] -= 1
            heapq.heappop(heap)

    def _rebalance(self):
        # want |lo| == |hi| or |lo| == |hi|+1
        if self.sz_lo > self.sz_hi + 1:
            v = -heapq.heappop(self.lo)
            self._prune(self.lo, self.del_lo)
            self.sum_lo -= v
            heapq.heappush(self.hi, v)
            self.sum_hi += v
            self.sz_lo -= 1
            self.sz_hi += 1
        elif self.sz_lo < self.sz_hi:
            v = heapq.heappop(self.hi)
            self._prune(self.hi, self.del_hi)
            self.sum_hi -= v
            heapq.heappush(self.lo, -v)
            self.sum_lo += v
            self.sz_hi -= 1
            self.sz_lo += 1

    def add(self, x):
        if not self.lo or x <= -self.lo[0]:
            heapq.heappush(self.lo, -x)
            self.sum_lo += x
            self.sz_lo += 1
        else:
            heapq.heappush(self.hi, x)
            self.sum_hi += x
            self.sz_hi += 1
        self._rebalance()

    def remove(self, x):
        # lazyâdelete x
        if x <= -self.lo[0]:
            self.del_lo[-x] += 1
            self.sum_lo -= x
            self.sz_lo -= 1
            self._prune(self.lo, self.del_lo)
        else:
            self.del_hi[x] += 1
            self.sum_hi -= x
            self.sz_hi -= 1
            self._prune(self.hi, self.del_hi)
        self._rebalance()

    def cost(self):
        # median = -self.lo[0]
        med = -self.lo[0]
        # sum |v-med| = med*|lo| - sum_lo  +  sum_hi - med*|hi|
        return med*self.sz_lo - self.sum_lo + self.sum_hi - med*self.sz_hi


class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        m = n - x + 1

        # 1) Slidingâwindow cost[i] = min ops to make nums[i:i+x] all equal.
        slide = SlidingMedian()
        cost = [0]*m

        # init window [0..x-1]
        for i in range(x):
            slide.add(nums[i])
        cost[0] = slide.cost()

        for i in range(1, m):
            slide.remove(nums[i-1])
            slide.add(nums[i+x-1])
            cost[i] = slide.cost()

        # 2) DP[j][i] = min cost to pick j windows among the first i (cost[0..i-1]).
        INF = 10**18
        prev = [0]*(m+1)      # dp[0][*] = 0
        curr = [INF]*(m+1)

        for j in range(1, k+1):
            curr[0] = INF
            for i in range(1, m+1):
                # skip window i-1:
                res = curr[i-1]
                # take window i-1, previous j-1 windows end before i-x
                take = prev[max(0, i-x)] + cost[i-1]
                curr[i] = min(res, take)
            prev, curr = curr, prev

        return prev[m]
