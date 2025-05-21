class Solution(object):
    def maxJump(self, stones):
        # initial jump for the first two stones
        res = stones[1] - stones[0]
        # consider jumps that skip one stone
        for i in range(2, len(stones)):
            res = max(res, stones[i] - stones[i-2])
        return res
