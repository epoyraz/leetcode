class Solution(object):
    def minOperations(self, nums):
        ans = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > prev:
                prev = nums[i]
            else:
                need = prev + 1
                ans += need - nums[i]
                prev = need
        return ans
