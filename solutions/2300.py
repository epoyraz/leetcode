from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s, repeatLimit):
        count = Counter(s)
        max_heap = [(-ord(c), c, count[c]) for c in count]
        heapq.heapify(max_heap)

        res = []

        while max_heap:
            _, ch, freq = heapq.heappop(max_heap)
            use = min(freq, repeatLimit)
            res.append(ch * use)
            freq -= use

            if freq > 0:
                if not max_heap:
                    break
                _, next_ch, next_freq = heapq.heappop(max_heap)
                res.append(next_ch)
                if next_freq > 1:
                    heapq.heappush(max_heap, (-ord(next_ch), next_ch, next_freq - 1))
                heapq.heappush(max_heap, (-ord(ch), ch, freq))

        return ''.join(res)
