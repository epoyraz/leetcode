import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([(w / float(q), q) for q, w in zip(quality, wage)])
        heap = []
        total_quality = 0
        res = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)

            if len(heap) == k:
                res = min(res, total_quality * ratio)

        return res
