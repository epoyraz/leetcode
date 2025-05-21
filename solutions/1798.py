class Solution(object):
    def maxOperations(self, nums, k):
        count = {}
        ops = 0
        for x in nums:
            need = k - x
            if count.get(need, 0) > 0:
                ops += 1
                count[need] -= 1
            else:
                count[x] = count.get(x, 0) + 1
        return ops
