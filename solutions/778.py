import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        
        if any(freq > (len(s) + 1) // 2 for freq in count.values()):
            return ""
        
        res = []
        while len(heap) >= 2:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)
            res.extend([char1, char2])
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, char2))
        
        if heap:
            res.append(heapq.heappop(heap)[1])
        
        return ''.join(res)
