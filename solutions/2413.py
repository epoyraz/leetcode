import heapq

class SmallestInfiniteSet:
    def __init__(self):
        # Min-heap of numbers that have been popped and then added back
        self.heap = []
        self.in_heap = set()
        # Next new number that has never been popped
        self.curr = 1

    def popSmallest(self):
        # If we've previously added back some smaller numbers, use those first
        if self.heap:
            x = heapq.heappop(self.heap)
            self.in_heap.remove(x)
            return x
        # Otherwise return the next fresh number
        x = self.curr
        self.curr += 1
        return x

    def addBack(self, num):
        # Only add back if it's strictly less than curr (i.e. was popped)
        # and not already in the heap
        if num < self.curr and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)
