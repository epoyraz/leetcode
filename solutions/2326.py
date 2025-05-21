class Solution(object):
    def sumScores(self, s):
        n = len(s)
        Z = [0] * n
        l = r = 0
        for i in xrange(1, n):
            if i <= r:
                k = i - l
                if Z[k] < r - i + 1:
                    Z[i] = Z[k]
                else:
                    j = r + 1
                    while j < n and s[j] == s[j - i]:
                        j += 1
                    Z[i] = j - i
                    l, r = i, j - 1
            else:
                j = 0
                while i + j < n and s[j] == s[i + j]:
                    j += 1
                Z[i] = j
                if j > 0:
                    l, r = i, i + j - 1
        return n + sum(Z)
