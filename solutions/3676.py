class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Let b = number of bits needed to represent n in binary,
        # i.e. b = floor(log2(n)) + 1
        b = n.bit_length()
        # candidate = 2^b - 1
        cand = (1 << b) - 1
        # if it's already >= n, that's our answer; otherwise we need one more bit
        if cand >= n:
            return cand
        else:
            return (1 << (b + 1)) - 1
