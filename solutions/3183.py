class Solution(object):
    def findKOr(self, nums, k):
        ans = 0
        # For each bit position 0 through 30
        for bit in range(31):
            # Count how many numbers have this bit set
            if sum((num >> bit) & 1 for num in nums) >= k:
                ans |= 1 << bit
        return ans