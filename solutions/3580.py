class Solution(object):
    def minStartingIndex(self, s, pattern):
        """
        :type s: str
        :type pattern: str
        :rtype: int
        """
        n, m = len(s), len(pattern)
        if m > n:
            return -1

        def z_algorithm(st):
            """Return Z-array for st in O(len(st))."""
            Z = [0] * len(st)
            Z[0] = len(st)
            l = r = 0
            for i in xrange(1, len(st)):
                if i <= r:
                    # we are inside a Z-box
                    k = i - l
                    Z[i] = min(Z[k], r - i + 1)
                # try to extend
                while i + Z[i] < len(st) and st[Z[i]] == st[i + Z[i]]:
                    Z[i] += 1
                if i + Z[i] - 1 > r:
                    l, r = i, i + Z[i] - 1
            return Z

        # 1) forward Z to get â[i] = Z at position (m+1+i)
        comb = pattern + '#' + s
        Z1 = z_algorithm(comb)
        # â[i] = longest match of pattern[0..] with s[i..]
        # starts at index (m+1) in Z1
        L = Z1[m+1 : m+1 + n]

        # 2) reverse both, do Z again to get suffix matches
        rs = s[::-1]
        rp = pattern[::-1]
        comb2 = rp + '#' + rs
        Z2 = z_algorithm(comb2)
        # for window at s[i..i+m-1], its reversed suffix starts at
        # rev index (n-1 - (i+m-1)) = n-m - i, which in comb2 is at m+1 + (n-m-i)
        R = [0] * (n - m + 1)
        base = m + 1
        for i in xrange(n - m + 1):
            R[i] = Z2[ base + (n - m - i) ]

        # 3) scan for the first i with at most one mismatch
        for i in xrange(n - m + 1):
            if L[i] == m or L[i] + R[i] >= m - 1:
                return i
        return -1