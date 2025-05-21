class Solution:
    def numberOfWays(self, startPos, endPos, k):
        mod = 10**9 + 7
        diff = endPos - startPos
        
        # r = number of right steps, l = number of left steps
        # r - l = diff, and r + l = k  =>  r = (k + diff)//2
        if (k + diff) % 2 != 0 or abs(diff) > k:
            return 0
        
        r = (k + diff) // 2
        if r < 0 or r > k:
            return 0
        
        # Precompute factorials and inverse factorials up to k
        fact = [1] * (k + 1)
        for i in range(1, k + 1):
            fact[i] = fact[i - 1] * i % mod
        
        invfact = [1] * (k + 1)
        invfact[k] = pow(fact[k], mod - 2, mod)
        for i in range(k, 0, -1):
            invfact[i - 1] = invfact[i] * i % mod
        
        # Compute C(k, r) = fact[k] * invfact[r] * invfact[k-r]
        return fact[k] * invfact[r] % mod * invfact[k - r] % mod
