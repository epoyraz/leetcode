class Solution:
    def prefixesDivBy5(self, nums):
        ans = []
        cur = 0
        for b in nums:
            cur = ((cur << 1) | b) % 5
            ans.append(cur == 0)
        return ans
