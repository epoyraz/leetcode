import heapq

class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        min_heap = []
        
        for i in range(len(heights) - 1):
            climb = heights[i+1] - heights[i]
            if climb > 0:
                heapq.heappush(min_heap, climb)
                # If we've used more climbs than ladders, pay the smallest with bricks
                if len(min_heap) > ladders:
                    bricks -= heapq.heappop(min_heap)
                    if bricks < 0:
                        # Can't afford even the smallest climb
                        return i
        # If we never ran out of resources, we reach the last building
        return len(heights) - 1
