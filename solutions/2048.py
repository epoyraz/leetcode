class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]
