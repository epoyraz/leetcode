class Solution:
    def maxSpending(self, values):
        """
        :type values: List[List[int]]
        :rtype: int
        """
        m = len(values)
        n = len(values[0]) if m else 0
        # Min-heap of (weight, shop_index, idx_in_shop)
        heap = []
        for i in range(m):
            # j = n-1 is the rightmost (smallest) available
            heap.append((values[i][n-1], i, n-1))
        heapq.heapify(heap)

        total = 0
        day = 1
        # We will schedule exactly m * n items
        for _ in range(m * n):
            w, i, j = heapq.heappop(heap)
            total += w * day
            day += 1
            # Advance to the next item in shop i, if any
            if j - 1 >= 0:
                heapq.heappush(heap, (values[i][j-1], i, j-1))

        return total
