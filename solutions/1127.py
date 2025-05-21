import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # max-heap via negatives
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = -heapq.heappop(heap)  # largest
            y = -heapq.heappop(heap)  # second largest
            if x != y:
                # remaining stone of weight |x - y|
                heapq.heappush(heap, -(x - y))
        return -heap[0] if heap else 0
