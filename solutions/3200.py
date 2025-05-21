class Solution:
    def stringCount(self, n):
        MOD = 10**9 + 7

        # fast modular exponentiation
        def mpow(a, b):
            res = 1
            a %= MOD
            while b:
                if b & 1:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                b >>= 1
            return res

        total = mpow(26, n)
        p25n = mpow(25, n)
        p25n1 = mpow(25, n - 1) if n > 0 else 0
        p24n = mpow(24, n)
        p24n1 = mpow(24, n - 1) if n > 0 else 0
        p23n = mpow(23, n)
        p23n1 = mpow(23, n - 1) if n > 0 else 0

        # inclusion-exclusion components
        A = p25n
        B = (p25n + n * p25n1) % MOD
        C = p25n
        AB = (p24n + n * p24n1) % MOD
        AC = p24n
        BC = (p24n + n * p24n1) % MOD
        # exclude 'l','t' and allow â¤1 'e'
        ABC = (p23n + n * p23n1) % MOD

        bad = (A + B + C - AB - AC - BC + ABC) % MOD
        return (total - bad) % MOD
