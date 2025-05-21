import heapq

class DinnerPlates(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.push_heap = []  # min-heap of indices that can accept pushes
        self.rightmost = -1

    def push(self, val):
        # Clean up invalid heap entries (full stacks)
        while self.push_heap and self.push_heap[0] < len(self.stacks) and len(self.stacks[self.push_heap[0]]) == self.capacity:
            heapq.heappop(self.push_heap)
        
        if self.push_heap:
            idx = heapq.heappop(self.push_heap)
            self.stacks[idx].append(val)
            heapq.heappush(self.push_heap, idx)
        else:
            self.stacks.append([val])
            idx = len(self.stacks) - 1
            if self.capacity > 1:
                heapq.heappush(self.push_heap, idx)

        self.rightmost = max(self.rightmost, idx)

    def pop(self):
        while self.rightmost >= 0 and (self.rightmost >= len(self.stacks) or not self.stacks[self.rightmost]):
            self.rightmost -= 1
        if self.rightmost < 0:
            return -1
        val = self.stacks[self.rightmost].pop()
        heapq.heappush(self.push_heap, self.rightmost)
        return val

    def popAtStack(self, index):
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        heapq.heappush(self.push_heap, index)
        if index == self.rightmost and not self.stacks[index]:
            while self.rightmost >= 0 and (self.rightmost >= len(self.stacks) or not self.stacks[self.rightmost]):
                self.rightmost -= 1
        return val
