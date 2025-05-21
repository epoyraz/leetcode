class Solution(object):
    def maximumXorProduct(self, a, b, n):
        MOD = 10**9 + 7
        x = 0
        for i in reversed(range(n)):
            bit = 1 << i
            with_bit = ((a ^ (x | bit)) * (b ^ (x | bit)))
            without_bit = ((a ^ x) * (b ^ x))
            if with_bit > without_bit:
                x |= bit
        return ((a ^ x) * (b ^ x)) % MOD