import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        heap = []
        total = 0
        
        for duration, lastDay in courses:
            total += duration
            heapq.heappush(heap, -duration)
            if total > lastDay:
                total += heapq.heappop(heap)
                
        return len(heap)
