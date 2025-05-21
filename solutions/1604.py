import collections
import heapq

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq = collections.Counter(arr)
        min_heap = list(freq.values())
        heapq.heapify(min_heap)

        while k > 0 and min_heap:
            cnt = heapq.heappop(min_heap)
            k -= cnt

        return len(min_heap) + (1 if k < 0 else 0)
