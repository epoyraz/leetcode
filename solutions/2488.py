import heapq

class Solution:
    def minGroups(self, intervals):
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        # Min-heap of end times of current overlapping group
        heap = []
        max_groups = 0

        for start, end in intervals:
            # Remove intervals that ended before this one starts (no overlap)
            while heap and heap[0] < start:
                heapq.heappop(heap)
            # Add this interval's end time
            heapq.heappush(heap, end)
            # The heap size is the number of overlapping intervals at this point
            max_groups = max(max_groups, len(heap))

        return max_groups
