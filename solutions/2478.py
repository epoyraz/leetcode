class Solution:
    def longestNiceSubarray(self, nums):
        l = 0
        curr = 0
        ans = 1
        for r, x in enumerate(nums):
            # If x conflicts with current window, shrink from left
            while (curr & x) != 0:
                curr ^= nums[l]
                l += 1
            # Add x into window
            curr |= x
            ans = max(ans, r - l + 1)
        return ans
