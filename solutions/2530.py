class Solution(object):
    def minimizeArrayValue(self, nums):
        prefix = 0
        res = 0
        for i, x in enumerate(nums):
            prefix += x
            # minimal max for this prefix is ceil(prefix/(i+1))
            # which is (prefix + i) // (i+1)
            val = (prefix + i) // (i + 1)
            if val > res:
                res = val
        return res
