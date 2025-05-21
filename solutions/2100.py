class Solution(object):
    def minNonZeroProduct(self, p):
        MOD = 10**9 + 7
        # M = 2^p
        M = 1 << p
        M1 = M - 1             # 2^p - 1
        base = M1 - 1          # 2^p - 2
        exp = (M1) // 2        # (2^p - 1)//2 = 2^{p-1} - 1
        return (M1 % MOD) * pow(base % MOD, exp, MOD) % MOD
