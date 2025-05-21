class Solution:
    def findValueOfPartition(self, nums):
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if diff < ans:
                ans = diff
        return ans
