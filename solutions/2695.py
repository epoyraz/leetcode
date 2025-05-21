import heapq

class Solution(object):
    def findScore(self, nums):
        n = len(nums)
        marked = [False] * n
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)

        score = 0
        marked_count = 0

        while marked_count < n:
            val, i = heapq.heappop(heap)
            if marked[i]:
                continue
            # pick this element
            score += val
            # mark i and its neighbors
            for j in (i-1, i, i+1):
                if 0 <= j < n and not marked[j]:
                    marked[j] = True
                    marked_count += 1

        return score
