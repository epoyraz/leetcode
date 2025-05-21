class Solution:
    def findFinalValue(self, nums, original):
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original
