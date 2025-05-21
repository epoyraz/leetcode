import heapq

class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days:   List[int]
        :rtype: int
        """
        n = len(apples)
        heap = []       # min-heap of (expire_day, count)
        day = 0
        eaten = 0
        
        # Continue while there are days left to grow apples or the heap is non-empty
        while day < n or heap:
            # 1) Add today's new batch if any
            if day < n and apples[day] > 0:
                expire = day + days[day]
                heapq.heappush(heap, (expire, apples[day]))
            
            # 2) Discard all rotten batches
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)
            
            # 3) Eat one apple from the batch that rots soonest
            if heap:
                expire, cnt = heapq.heappop(heap)
                # eat one
                eaten += 1
                if cnt > 1:
                    # push back with one fewer apple
                    heapq.heappush(heap, (expire, cnt - 1))
            
            # 4) Move to the next day
            day += 1
        
        return eaten
