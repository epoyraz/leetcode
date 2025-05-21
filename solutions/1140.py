import heapq
from collections import Counter

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        count = Counter(barcodes)
        # Max-heap based on frequency
        max_heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(max_heap)

        result = []
        
        while len(max_heap) >= 2:
            freq1, num1 = heapq.heappop(max_heap)
            freq2, num2 = heapq.heappop(max_heap)
            
            result.extend([num1, num2])
            
            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, num1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, num2))

        if max_heap:
            result.append(max_heap[0][1])
        
        return result
