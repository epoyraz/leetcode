class Solution:
    def findClosestNumber(self, nums):
        best = nums[0]
        for x in nums:
            if abs(x) < abs(best) or (abs(x) == abs(best) and x > best):
                best = x
        return best
