from bisect import bisect_left, insort

class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        if x == 0:
            return 0

        s = []
        res = float('inf')
        for i in range(x, len(nums)):
            insort(s, nums[i - x])
            idx = bisect_left(s, nums[i])
            if idx < len(s):
                res = min(res, abs(s[idx] - nums[i]))
            if idx > 0:
                res = min(res, abs(s[idx - 1] - nums[i]))
        return res
