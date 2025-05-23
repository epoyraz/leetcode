class Solution(object):
    def findTheArrayConcVal(self, nums):
        res = 0
        l, r = 0, len(nums) - 1
        while l < r:
            res += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        if l == r:
            res += nums[l]
        return res
