import heapq
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        self.index_to_num = {}
        self.num_to_heap = defaultdict(list)

    def change(self, index, number):
        old = self.index_to_num.get(index)
        if old == number:
            return
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number):
        heap = self.num_to_heap.get(number, [])
        while heap:
            idx = heap[0]
            if self.index_to_num.get(idx) == number:
                return idx
            heapq.heappop(heap)
        return -1
