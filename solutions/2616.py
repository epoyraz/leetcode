import heapq
import math

class Solution:
    def maxKelements(self, nums, k):
        # Use a max-heap by pushing negative values
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        
        score = 0
        for _ in range(k):
            top = -heapq.heappop(max_heap)
            score += top
            # Push updated value back
            heapq.heappush(max_heap, -((top + 2) // 3))  # equivalent to ceil(top / 3)
        
        return score
