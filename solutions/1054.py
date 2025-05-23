class Solution:
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        mask = (1 << n.bit_length()) - 1
        return n ^ mask
