import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        l, r = 0, n - 1
        left_heap = []  # (cost, index)
        right_heap = []

        # Initialize heaps with up to 'candidates' from each end
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, (costs[l], l))
                l += 1
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(right_heap, (costs[r], r))
                r -= 1

        total = 0
        # Hire k workers
        for _ in range(k):
            # Decide from which heap to pick
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                cost, idx = heapq.heappop(left_heap)
                total += cost
                # Refill from left side if possible
                if l <= r:
                    heapq.heappush(left_heap, (costs[l], l))
                    l += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total += cost
                # Refill from right side if possible
                if l <= r:
                    heapq.heappush(right_heap, (costs[r], r))
                    r -= 1

        return total
