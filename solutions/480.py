import heapq
from collections import defaultdict

class DualHeap:
    def __init__(self, k):
        self.small = []  # max heap (invert values)
        self.large = []  # min heap
        self.delayed = defaultdict(int)
        self.k = k
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num]:
                heapq.heappop(heap)
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
            else:
                break

    def balance(self):
        if self.small_size > self.large_size:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
        elif self.large_size > self.small_size + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.large_size -= 1
            self.small_size += 1

        self.prune(self.small)
        self.prune(self.large)

    def insert(self, num):
        if not self.large or num >= self.large[0]:
            heapq.heappush(self.large, num)
            self.large_size += 1
        else:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        self.balance()

    def erase(self, num):
        self.delayed[num] += 1
        if self.large and num >= self.large[0]:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)
        else:
            self.small_size -= 1
            if self.small and num == -self.small[0]:
                self.prune(self.small)
        self.balance()

    def get_median(self):
        self.prune(self.small)
        self.prune(self.large)
        if self.k % 2 == 1:
            return float(self.large[0])
        return (self.large[0] - self.small[0]) / 2.0


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        dh = DualHeap(k)
        for i in range(k):
            dh.insert(nums[i])
        res = [dh.get_median()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            res.append(dh.get_median())
        return res
