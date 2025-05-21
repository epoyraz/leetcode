class Solution(object):
    def minimizeSum(self, nums):
        nums.sort()
        n = len(nums)
        # remove two smallest, two largest, or one of each
        return min(
            nums[n-3] - nums[0],
            nums[n-2] - nums[1],
            nums[n-1] - nums[2]
        )
