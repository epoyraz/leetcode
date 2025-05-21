import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        res = [[0, 0]]
        heap = [(0, float('inf'))]

        for x, neg_h, r in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_h:
                heapq.heappush(heap, (neg_h, r))
            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])

        return res[1:]
