class Solution(object):
    def triangularSum(self, nums):
        while len(nums) > 1:
            nums = [(nums[i] + nums[i+1]) % 10 for i in xrange(len(nums) - 1)]
        return nums[0]
