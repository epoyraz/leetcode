class Solution:
    def waysToSplitArray(self, nums):
        total = sum(nums)
        count = 0
        prefix = 0
        # we can split at i for i in [0..n-2]
        for i in range(len(nums) - 1):
            prefix += nums[i]
            # check prefix >= suffix
            if prefix * 2 >= total:
                count += 1
        return count
