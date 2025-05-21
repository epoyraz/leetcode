class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        res = 0
        prev_count = 0
        j = 0
        
        for i in range(len(nums)):
            if left <= nums[i] <= right:
                prev_count = i - j + 1
                res += prev_count
            elif nums[i] < left:
                res += prev_count
            else:
                prev_count = 0
                j = i + 1
        
        return res
