class Solution(object):
    def minMaxSums(self, nums, k):
        """
        :type nums: List[int]
        :type k:    int
        :rtype:     int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # 1) Precompute factorials & inv-factorials up to n
        fac    = [1] * (n+1)
        invfac = [1] * (n+1)
        for i in range(1, n+1):
            fac[i] = fac[i-1] * i % MOD
        invfac[n] = pow(fac[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfac[i-1] = invfac[i] * i % MOD
        
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fac[a] * invfac[b] % MOD * invfac[a-b] % MOD
        
        # 2) Precompute f(i) = sum_{t=0..min(i,k-1)} C(i, t)
        f = [0] * n
        # powers of 2 up to k-1
        pow2 = [1] * k
        for i in range(1, k):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        for i in range(n):
            if i < k:
                # f(i) = 2^i
                f[i] = pow2[i]
            else:
                # f(i) = 2*f(i-1) - C(i-1, k-1)
                val = (2 * f[i-1] - comb(i-1, k-1)) % MOD
                f[i] = val
        
        # 3) Sort the array
        A = sorted(nums)
        
        # 4) Sum up max-contributions and min-contributions
        ans = 0
        for i, v in enumerate(A):
            ans = (ans + v * f[i] + v * f[n-1-i]) % MOD
        
        return ans
