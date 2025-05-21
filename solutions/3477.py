class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flips = 0
        parity = 0      # how many flips we've done so far, mod 2
        for x in nums:
            # x ^ parity is the effective bit after applying all previous suffix-flips
            if x ^ parity == 0:
                flips += 1
                parity ^= 1
        return flips
