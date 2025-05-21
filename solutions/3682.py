class Solution(object):
    def countGoodArrays(self, n, m, k):
        MOD = 10**9 + 7
        
        # Precompute factorials + inverses up to n:
        fact = [1] * (n)
        inv_fact = [1] * (n)
        for i in range(1, n):
            fact[i] = fact[i-1] * i % MOD
        
        # Fermatâs little theorem for inverses:
        inv_fact[n-1] = pow(fact[n-1], MOD-2, MOD)
        for i in range(n-1, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD
        
        # Binomial helper: C(a, b) with 0 <= b <= a < n
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a-b] % MOD
        
        # Number of segments = n - k
        # Answer = C(n-1, k) * m * (m-1)^(n-k-1)
        return (
            comb(n-1, k)
            * m
            % MOD
            * pow(m-1, n-k-1, MOD)
            % MOD
        )
