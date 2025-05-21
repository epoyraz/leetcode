class Solution:
    def countSubstrings(self, s, t):
        m, n = len(s), len(t)
        res = 0
        for i in range(m):
            for j in range(n):
                mismatch = 0
                k = 0
                # Extend substring as long as we have at most one mismatch
                while i + k < m and j + k < n:
                    if s[i+k] != t[j+k]:
                        mismatch += 1
                    if mismatch > 1:
                        break
                    if mismatch == 1:
                        res += 1
                    k += 1
        return res
