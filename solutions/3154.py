class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[i] - nums[j]
                if diff <= 0:
                    continue
                for k in range(j+1, n):
                    val = diff * nums[k]
                    if val > res:
                        res = val
        return res