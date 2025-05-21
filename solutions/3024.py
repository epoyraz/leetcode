class Solution:
    MOD = 10**9 + 7

    def numberOfWays(self, s, t, k):
        n = len(s)
        # 1) Find all rotations d in [0..n-1] with rotateRight(s,d)==t via KMP
        # Build prefix-function on pattern t
        def kmp_prefix(p):
            m = len(p)
            pi = [0]*m
            j = 0
            for i in range(1, m):
                while j and p[i] != p[j]:
                    j = pi[j-1]
                if p[i] == p[j]:
                    j += 1
                pi[i] = j
            return pi

        pi = kmp_prefix(t)
        D0 = 0
        Dnz = 0
        j = 0
        ss = s + s
        for i, ch in enumerate(ss):
            # only consider matches completing at i with start = i - (n-1) < n
            while j and ch != t[j]:
                j = pi[j-1]
            if ch == t[j]:
                j += 1
                if j == n:
                    start = i - (n - 1)
                    if start < n:
                        if start % n == 0:
                            D0 += 1
                        else:
                            Dnz += 1
                    j = pi[j-1]

        if D0 + Dnz == 0:
            return 0

        # 2) Compute F_k(0) and F_k(nonzero) in Z_n*
        M = n - 1
        Mk = pow(M, k, self.MOD)
        neg1k = 1 if (k & 1) == 0 else self.MOD - 1
        inv_n = pow(n, self.MOD - 2, self.MOD)

        F0 = (Mk + (n - 1) * neg1k) % self.MOD * inv_n % self.MOD
        F1 = (Mk - neg1k) % self.MOD * inv_n % self.MOD

        # Total ways = D0*F0 + Dnz*F1 mod
        return (D0 * F0 + Dnz * F1) % self.MOD
