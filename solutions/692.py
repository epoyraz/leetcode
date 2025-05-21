import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
