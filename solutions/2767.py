import heapq

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Use a max-heap (invert signs for Python's min-heap)
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        score = 0
        for _ in range(k):
            # Pop the largest element
            m = -heapq.heappop(max_heap)
            score += m
            # Increment it by 1 and push back
            heapq.heappush(max_heap, -(m + 1))

        return score
