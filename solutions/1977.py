import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort(key=lambda x: x[0])
        sorted_q = sorted([(q, i) for i, q in enumerate(queries)])
        ans = [-1] * len(queries)
        heap = []
        idx = 0
        n = len(intervals)
        
        for q, qi in sorted_q:
            while idx < n and intervals[idx][0] <= q:
                l, r = intervals[idx]
                size = r - l + 1
                heapq.heappush(heap, (size, r))
                idx += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                ans[qi] = heap[0][0]
        return ans
