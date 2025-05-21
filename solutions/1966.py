class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        left = 0
        total = 0
        res = 1
        for right, x in enumerate(nums):
            total += x
            # cost to make all in window [left..right] equal to x
            cost = x * (right - left + 1) - total
            while cost > k:
                total -= nums[left]
                left += 1
                cost = x * (right - left + 1) - total
            res = max(res, right - left + 1)
        return res
