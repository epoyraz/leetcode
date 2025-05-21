class Solution(object):
    def getMinDistance(self, nums, target, start):
        return min(abs(i - start) for i, v in enumerate(nums) if v == target)
