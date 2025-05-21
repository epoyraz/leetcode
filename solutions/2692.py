import heapq
import math

class Solution(object):
    def pickGifts(self, gifts, k):
        # Use max-heap by negating values
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            max_gift = -heapq.heappop(heap)
            reduced = int(math.sqrt(max_gift))
            heapq.heappush(heap, -reduced)

        return -sum(heap)
