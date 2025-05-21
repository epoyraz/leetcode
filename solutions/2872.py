class Solution:
    def maxArrayValue(self, nums):
        total = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= total:
                total += nums[i]
            else:
                total = nums[i]
        return total
