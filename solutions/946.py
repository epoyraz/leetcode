class Solution:
    def smallestRangeII(self, nums, k):
        nums.sort()
        # initial score without changes
        ans = nums[-1] - nums[0]
        n = len(nums)
        # try splitting between i and i+1
        for i in range(n - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low  = min(nums[0] + k, nums[i+1] - k)
            ans = min(ans, high - low)
        return ans
