class Solution(object):
    def shortestMatchingSubstring(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: int
        """
        n = len(s)

        # Split p into A, B, C around the two '*' characters
        parts = p.split('*')
        A, B, C = parts[0], parts[1], parts[2]

        # Helper: compute all match positions of pattern pat in text s
        # Returns a boolean list match of length n+1, where match[i] is True
        # iff s[i:i+len(pat)] == pat.  Empty pat matches everywhere.
        def compute_matches(pat):
            m = len(pat)
            if m == 0:
                return [True] * (n + 1)
            # Build LPS array for KMP
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            # KMP search
            match = [False] * (n + 1)
            j = 0  # index in pat
            i = 0  # index in s
            while i < n:
                if s[i] == pat[j]:
                    i += 1
                    j += 1
                    if j == m:
                        # match ends at i, starts at i-m
                        match[i - m] = True
                        j = lps[j - 1]
                else:
                    if j:
                        j = lps[j - 1]
                    else:
                        i += 1
            return match

        matchA = compute_matches(A)
        matchB = compute_matches(B)
        matchC = compute_matches(C)

        INF = n + 1

        # Build next-occurrence arrays for B and C
        nxtB = [INF] * (n + 2)
        nxtC = [INF] * (n + 2)
        # We only need to fill up to index n
        for i in range(n, -1, -1):
            if i < n + 1 and matchB[i]:
                nxtB[i] = i
            else:
                nxtB[i] = nxtB[i + 1]
            if i < n + 1 and matchC[i]:
                nxtC[i] = i
            else:
                nxtC[i] = nxtC[i + 1]

        ans = INF
        lenA, lenB, lenC = len(A), len(B), len(C)

        # Try every start index i where A matches
        for i in range(0, n + 1):
            if not matchA[i]:
                continue
            # substring must start at i, so A occupies [i, i+lenA)
            a_end = i + lenA
            if a_end > n:
                continue
            # find B at j >= a_end
            j = nxtB[a_end]
            if j > n:
                continue
            b_end = j + lenB
            if b_end > n:
                continue
            # find C at k >= b_end
            k = nxtC[b_end]
            if k > n:
                continue
            t_end = k + lenC
            if t_end > n:
                continue
            # candidate substring is s[i:t_end], length t_end - i
            length = t_end - i
            if length < ans:
                ans = length

        return ans if ans <= n else -1
