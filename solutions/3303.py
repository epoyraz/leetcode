class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        def kmp_search(text, pat):
            """Return list of all startâindices where pat occurs in text."""
            n, m = len(text), len(pat)
            # Build LPS array for pat
            lps = [0]*m
            length = 0
            i = 1
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length:
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1
            # KMP scan
            res = []
            i = j = 0
            while i < n:
                if text[i] == pat[j]:
                    i += 1
                    j += 1
                    if j == m:
                        res.append(i-j)
                        j = lps[j-1]
                else:
                    if j:
                        j = lps[j-1]
                    else:
                        i += 1
            return res

        # 1) Find all start indices of 'a' and 'b' in s
        posA = kmp_search(s, a)
        posB = kmp_search(s, b)

        # If b never occurs, no i can be beautiful
        if not posB:
            return []

        # 2) Twoâpointer sweep to check for each i in posA
        #    whether thereâs some j in posB with |j-i| <= k.
        res = []
        j = 0
        m = len(posB)
        for i in posA:
            # advance j until posB[j] >= i-k
            while j < m and posB[j] < i - k:
                j += 1
            # now posB[j] is the first candidate â¥ i-k
            if j < m and posB[j] <= i + k:
                res.append(i)

        return res
