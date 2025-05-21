MOD = 10**9 + 7

class Solution(object):
    def makeStringSorted(self, s):
        n = len(s)
        # precompute factorials and inverse factorials
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (n+1)
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD

        # frequency of each character
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # denom = product of invfact[freq[c]] for all c
        denom = 1
        for c in range(26):
            denom = denom * invfact[freq[c]] % MOD

        rank = 0
        rem = n
        for ch in s:
            cidx = ord(ch) - ord('a')
            rem -= 1
            # count characters smaller than ch
            for c in range(cidx):
                if freq[c] > 0:
                    # number of perms if we put char c here
                    # = fact[rem] * denom' where denom' = denom * fact[freq[c]] * invfact[freq[c]-1]
                    add = fact[rem] * denom % MOD
                    add = add * fact[freq[c]] % MOD
                    add = add * invfact[freq[c]-1] % MOD
                    rank = (rank + add) % MOD
            # fix ch at this position: update denom and freq
            denom = denom * fact[freq[cidx]] % MOD
            denom = denom * invfact[freq[cidx]-1] % MOD
            freq[cidx] -= 1

        return rank
