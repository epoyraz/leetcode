class Solution(object):
    def countVowelPermutation(self, n):
        MOD = 10**9 + 7

        a = e = i = o = u = 1

        for _ in range(1, n):
            a_new = (e + i + u) % MOD
            e_new = (a + i) % MOD
            i_new = (e + o) % MOD
            o_new = i % MOD
            u_new = (i + o) % MOD

            a, e, i, o, u = a_new, e_new, i_new, o_new, u_new

        return (a + e + i + o + u) % MOD
