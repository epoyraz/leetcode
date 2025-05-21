import heapq
from collections import defaultdict

class Solution(object):
    def findMaximumElegance(self, items, k):
        items.sort(reverse=True)  # sort by profit descending
        used = set()
        dup_heap = []
        total = 0
        res = 0

        for i in range(k):
            profit, cat = items[i]
            total += profit
            if cat in used:
                heapq.heappush(dup_heap, profit)
            else:
                used.add(cat)

        res = total + len(used) * len(used)

        j = k
        while j < len(items) and dup_heap:
            profit, cat = items[j]
            if cat in used:
                j += 1
                continue
            removed = heapq.heappop(dup_heap)
            total += profit - removed
            used.add(cat)
            res = max(res, total + len(used) * len(used))
            j += 1

        return res
