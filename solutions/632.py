import heapq

class Solution(object):
    def smallestRange(self, nums):
        heap = []
        max_val = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        
        result = [float('-inf'), float('inf')]
        
        while True:
            min_val, row, idx = heapq.heappop(heap)
            if max_val - min_val < result[1] - result[0] or (max_val - min_val == result[1] - result[0] and min_val < result[0]):
                result = [min_val, max_val]
            if idx + 1 == len(nums[row]):
                break
            next_val = nums[row][idx + 1]
            heapq.heappush(heap, (next_val, row, idx + 1))
            max_val = max(max_val, next_val)
        
        return result
