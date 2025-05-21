class Solution(object):
    def numOfWays(self, nums):
        mod = 10**9 + 7
        n = len(nums)
        # precompute factorials and inverse factorials
        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i-1] * i % mod
        invfac = [1] * (n + 1)
        invfac[n] = pow(fac[n], mod-2, mod)
        for i in range(n, 0, -1):
            invfac[i-1] = invfac[i] * i % mod

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fac[a] * invfac[b] % mod * invfac[a-b] % mod

        def dfs(arr):
            m = len(arr)
            if m <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            wl = dfs(left)
            wr = dfs(right)
            return wl * wr % mod * comb(len(left) + len(right), len(left)) % mod

        return (dfs(nums) - 1) % mod
