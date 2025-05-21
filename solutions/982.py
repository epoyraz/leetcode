class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0
        prev = -1  # the last assigned unique value
        for x in nums:
            # each x must be at least prev + 1
            target = max(x, prev + 1)
            moves += target - x
            prev = target
        return moves
