class Solution:
    def subArrayRanges(self, nums):
        total = 0
        n = len(nums)

        for i in range(n):
            max_val = min_val = nums[i]
            for j in range(i, n):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])
                total += max_val - min_val

        return total
