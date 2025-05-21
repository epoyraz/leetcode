import heapq

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3
        
        # Prefix: max heap to track smallest n elements from the left
        left_heap = []
        left_sum = 0
        prefix = [0] * (2 * n + 1)
        
        for i in range(2 * n):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i]
            if len(left_heap) > n:
                left_sum += heapq.heappop(left_heap)  # Remove largest (smallest negative)
            if len(left_heap) == n:
                prefix[i + 1] = left_sum
        
        # Suffix: min heap to track largest n elements from the right
        right_heap = []
        right_sum = 0
        suffix = [0] * (2 * n + 1)
        
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            if len(right_heap) > n:
                right_sum -= heapq.heappop(right_heap)
            if len(right_heap) == n:
                suffix[i] = right_sum
        
        # Find minimum difference
        res = float('inf')
        for i in range(n, 2 * n + 1):
            res = min(res, prefix[i] - suffix[i])
        
        return res
