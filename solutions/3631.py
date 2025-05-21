class Solution(object):
    def countKReducibleNumbers(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)

        # Precompute factorials and inv factorials for C(n, k)
        max_n = n
        fact = [1] * (max_n + 1)
        inv  = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        inv[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n, 0, -1):
            inv[i-1] = inv[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv[b] % MOD * inv[a-b] % MOD

        # Precompute f[c] = # operations to reduce c â 1 by replacing with popcount
        pop = [bin(i).count('1') for i in range(n+1)]
        f   = [-1] * (n+1)
        f[1] = 0
        def getf(x):
            if f[x] != -1:
                return f[x]
            f[x] = 1 + getf(pop[x])
            return f[x]
        for i in range(2, n+1):
            getf(i)

        # Which popcounts p satisfy 1 + f(p) â¤ k  â  f(p) â¤ k-1
        good = [False] * (n+1)
        for p in range(1, n+1):
            if f[p] <= k-1:
                good[p] = True

        # DP to count how many x < s have exactly p ones
        counts = [0] * (n+1)
        ones_so_far = 0
        for i, ch in enumerate(s):
            if ch == '1':
                rem = n - i - 1
                for j in range(rem+1):
                    counts[ones_so_far + j] = (counts[ones_so_far + j] + comb(rem, j)) % MOD
                ones_so_far += 1

        # Exclude x = 0 (popcount = 0), since we only want positive integers
        counts[0] = 0

        # Sum over all popcounts that are âgoodâ
        ans = 0
        for p in range(1, n+1):
            if good[p]:
                ans = (ans + counts[p]) % MOD

        return ans
