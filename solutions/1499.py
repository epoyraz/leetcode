import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        max_perf = total_speed = 0
        heap = []

        for e, s in engineers:
            heapq.heappush(heap, s)
            total_speed += s
            if len(heap) > k:
                total_speed -= heapq.heappop(heap)
            max_perf = max(max_perf, total_speed * e)

        return max_perf % MOD
