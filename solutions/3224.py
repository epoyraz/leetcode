class Solution(object):
    def numberOfSequence(self, n, sick):
        """
        :type n: int
        :type sick: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        m = len(sick)
        # Build segment lengths
        segments = []
        # left end
        segments.append(sick[0])
        # interior segments
        for i in range(1, m):
            segments.append(sick[i] - sick[i-1] - 1)
        # right end
        segments.append(n - 1 - sick[-1])
        # total uninfected
        M = n - m

        # Precompute factorials and inverse factorials up to n
        fac = [1] * (n+1)
        ifac = [1] * (n+1)
        for i in range(1, n+1):
            fac[i] = fac[i-1] * i % mod
        ifac[n] = pow(fac[n], mod-2, mod)
        for i in range(n, 0, -1):
            ifac[i-1] = ifac[i] * i % mod

        # Multinomial coefficient: M! / (prod L_i!)
        res = fac[M]
        for L in segments:
            res = res * ifac[L] % mod

        # For each interior segment (not the first or last), multiply by 2^(L-1)
        for L in segments[1:-1]:
            if L > 0:
                res = res * pow(2, L-1, mod) % mod

        return res
