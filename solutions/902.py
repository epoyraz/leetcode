import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        max_heap = []
        i = 0
        fuel = startFuel
        stops = 0
        
        while fuel < target:
            while i < len(stations) and stations[i][0] <= fuel:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            if not max_heap:
                return -1
            fuel += -heapq.heappop(max_heap)
            stops += 1
        
        return stops
