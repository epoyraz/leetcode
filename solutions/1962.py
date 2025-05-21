import heapq

class Solution(object):
    def getOrder(self, tasks):
        # tasks: List[List[int]]
        n = len(tasks)
        # augment with original indices and sort by enqueue time
        arr = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        heap = []
        time = 0
        i = 0
        res = []
        while i < n or heap:
            if not heap and time < arr[i][0]:
                time = arr[i][0]
            while i < n and arr[i][0] <= time:
                _, pt, idx = arr[i]
                heapq.heappush(heap, (pt, idx))
                i += 1
            pt, idx = heapq.heappop(heap)
            time += pt
            res.append(idx)
        return res
