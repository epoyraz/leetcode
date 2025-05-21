import heapq

class Solution(object):
    def minimumDeviation(self, nums):
        # initialize max-heap and track current minimum
        heap = []
        mi = float('inf')
        for x in nums:
            if x % 2:      # make all numbers even
                x *= 2
            heap.append(-x)
            mi = min(mi, x)
        heapq.heapify(heap)
        
        # initial deviation
        res = -heap[0] - mi
        
        # keep reducing the maximum until it's odd
        while True:
            x = -heapq.heappop(heap)
            res = min(res, x - mi)
            if x % 2:      # can't reduce further
                break
            x //= 2
            mi = min(mi, x)
            heapq.heappush(heap, -x)
        
        return res
