import bisect

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        res = 0
        for i in xrange(n):
            lo = lower - nums[i]
            hi = upper - nums[i]
            left = bisect.bisect_left(nums, lo, i+1, n)
            right = bisect.bisect_right(nums, hi, i+1, n)
            res += right - left
        return res
