class Solution:
    def minPairSum(self, nums):
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[-1 - i])
        return ans
