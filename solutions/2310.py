import heapq

class Solution(object):
    def halveArray(self, nums):
        total = sum(nums)
        target = total / 2.0
        heap = [-float(x) for x in nums]
        heapq.heapify(heap)
        
        ops = 0
        reduced = 0.0

        while reduced < target:
            x = -heapq.heappop(heap)
            x /= 2.0
            reduced += x
            heapq.heappush(heap, -x)
            ops += 1

        return ops
