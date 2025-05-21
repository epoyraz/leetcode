class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        Z, O, L = zero, one, limit
        N = Z + O

        # Precompute factorials and inverse factorials up to N+N
        M = 2 * N + 5
        fact = [1] * M
        invfact = [1] * M
        for i in range(1, M):
            fact[i] = fact[i-1] * i % MOD
        invfact[M-1] = pow(fact[M-1], MOD-2, MOD)
        for i in range(M-2, -1, -1):
            invfact[i] = invfact[i+1] * (i+1) % MOD

        def binom(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * invfact[k] % MOD * invfact[n-k] % MOD

        # Count compositions of n into k positive parts, each â¤ L
        def count_bounded(n, k):
            if k == 0:
                return 1 if n == 0 else 0
            # sum_{j=0..floor((n-k)/L)} (-1)^j * C(k, j) * C(n - jL -1, k-1)
            res = 0
            maxj = (n - k) // L
            for j in range(maxj + 1):
                term = binom(k, j) * binom(n - j*L - 1, k - 1) % MOD
                if j & 1:
                    res = (res - term) % MOD
                else:
                    res = (res + term) % MOD
            return res

        ans = 0
        # Try both possible starting bits s=0 or s=1
        for s in (0, 1):
            # total number of blocks K from 1 up to N
            for K in range(1, N+1):
                # zero-blocks / one-blocks depending on start
                if s == 0:
                    Zb = (K + 1) // 2
                    Ob = K // 2
                else:
                    Zb = K // 2
                    Ob = (K + 1) // 2

                if Zb > Z or Ob > O:
                    continue

                ways_z = count_bounded(Z, Zb)
                ways_o = count_bounded(O, Ob)
                ans = (ans + ways_z * ways_o) % MOD

        return ans

