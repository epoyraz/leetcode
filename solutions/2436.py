class Solution:
    def minimumOperations(self, nums):
        # Count how many distinct positive values there are
        return len({x for x in nums if x > 0})
