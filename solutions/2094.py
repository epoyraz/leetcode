import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        # Use a max-heap by pushing negatives
        heap = [-p for p in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            # Pop the largest pile
            p = -heapq.heappop(heap)
            # Remove floor(p/2), new size is ceil(p/2)
            new_p = (p + 1) // 2
            # Push back
            heapq.heappush(heap, -new_p)
        
        # Sum remaining stones
        return -sum(heap)
