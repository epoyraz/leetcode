class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for num in nums:
            res = -1
            for k in range(num.bit_length()):
                x = num - (1 << k)
                if x < 0:
                    continue
                if (x | (x + 1)) == num:
                    if res == -1 or x < res:
                        res = x
            ans.append(res)
        return ans
