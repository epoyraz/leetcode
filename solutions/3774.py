class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        # Compute the 'delta' array D[i] = s[i]-s[i+1] mod 10
        D = [ (int(s[i]) - int(s[i+1])) % 10
              for i in range(n-1) ]
        N = n-2

        # 1) Sum mod 2: binom(N,i)%2 == 1 iff (i & (N-i))==0
        S2 = 0
        for i, d in enumerate(D):
            if (i & (N - i)) == 0:
                S2 = (S2 + d) & 1

        # 2) Sum mod 5: use Lucas to get C(N, i) mod 5
        # Precompute binomial(n,k)%5 for n,k<5
        small = [[0]*5 for _ in range(5)]
        for a in range(5):
            small[a][0] = 1
            for b in range(1, a+1):
                small[a][b] = (small[a-1][b-1] + small[a-1][b]) % 5

        # base-5 digits of N
        ND = []
        tmp = N
        while tmp:
            ND.append(tmp % 5)
            tmp //= 5
        if not ND:
            ND = [0]

        def binom5(N, i):
            """Return C(N,i) mod 5 by Lucas."""
            res = 1
            pos = 0
            while N or i:
                n_k = N % 5
                i_k = i % 5
                # if i_k > n_k then C=0
                if i_k > n_k:
                    return 0
                res = (res * small[n_k][i_k]) % 5
                N //= 5
                i //= 5
            return res

        S5 = 0
        for i, d in enumerate(D):
            c5 = binom5(N, i)
            if c5:
                S5 = (S5 + c5 * d) % 5

        # Reconstruct x mod 10 with
        #   x â¡ S2 (mod 2),
        #   x â¡ S5 (mod 5).
        # Two candidates: S5 or S5+5; pick the one matching parity S2.
        x = S5
        if x % 2 != S2:
            x += 5

        return (x % 10) == 0
