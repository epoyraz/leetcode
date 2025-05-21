import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        ops = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = 2 * x + y
            heapq.heappush(nums, new_val)
            ops += 1
        return ops
