class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0
        
        for i, x in enumerate(nums):
            # right sum = total - left_sum - x
            if left_sum == total - left_sum - x:
                return i
            left_sum += x
        
        return -1
