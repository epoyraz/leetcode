class Solution(object):
    def concatenatedBinary(self, n):
        mod = 10**9 + 7
        res = 0
        for i in range(1, n + 1):
            # shift left by the bit-length of i, then add i
            res = ((res << i.bit_length()) + i) % mod
        return res
