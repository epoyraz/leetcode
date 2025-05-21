class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n < 3:
            return n
        p = 1 << (n.bit_length() - 1)
        return 2 * p
