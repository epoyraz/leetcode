class Solution:
    def maximumXOR(self, nums):
        ans = 0
        for v in nums:
            ans |= v
        return ans
