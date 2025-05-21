class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        res = [0] * n
        total = prefix[n]
        for i, v in enumerate(nums):
            # sum of differences for elements before i
            left = v * i - prefix[i]
            # sum of differences for elements after i
            right = (total - prefix[i+1]) - v * (n - i - 1)
            res[i] = left + right
        return res
