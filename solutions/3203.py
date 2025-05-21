class Solution(object):
    def canMakePalindromeQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        half = n // 2

        # 1) Build prefixâcounts for each letter over the whole string
        #    prefix[ch][i] = count of letter ch in s[0:i]
        prefix = [[0]*(n+1) for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            for c in range(26):
                prefix[c][i+1] = prefix[c][i]
            prefix[idx][i+1] += 1

        # 2) Build a mismatch array for the first half,
        #    mismatch[i] = 1 if s[i] != s[n-1-i], else 0
        mismatch = [0]*half
        for i in range(half):
            if s[i] != s[n-1-i]:
                mismatch[i] = 1

        # 3) Build its prefixâsum so we can query any subârange
        pm = [0]*(half+1)
        for i in range(half):
            pm[i+1] = pm[i] + mismatch[i]
        total_mismatch = pm[half]

        ans = []
        for a, b, c, d in queries:
            # ----  Step A: Check fixedâoutside windows are already palindromic  ----
            # I1 = [a..b] in left half,   I2 = mirror of [c..d] is [n-1-d..n-1-c]
            i1_l, i1_r = a, b
            i2_l, i2_r = n-1-d, n-1-c

            # mismatches inside I1
            m1 = pm[i1_r+1] - pm[i1_l]
            # mismatches inside I2
            m2 = pm[i2_r+1] - pm[i2_l]
            # but I1 and I2 may overlap; subtract their intersection once
            ol = max(i1_l, i2_l)
            or_ = min(i1_r, i2_r)
            mo = 0
            if ol <= or_:
                mo = pm[or_+1] - pm[ol]

            if m1 + m2 - mo != total_mismatch:
                # Some mismatch cannot be fixed since neither position is in a movable window
                ans.append(False)
                continue

            # ----  Step B: Count how many chars we must âuse upâ to match fixed partners  ----
            # L window = [a..b],   R window = [c..d]
            # Mirror of L is M1 = [n-1-b..n-1-a]
            # Mirror of R is M2 = [n-1-d..n-1-c]
            m1_l, m1_r = n-1-b, n-1-a
            m2_l, m2_r = i2_l, i2_r

            # 1) Multiset of chars in each window
            Lcnt = [0]*26
            Rcnt = [0]*26
            for ch in range(26):
                Lcnt[ch] = prefix[ch][b+1] - prefix[ch][a]
                Rcnt[ch] = prefix[ch][d+1] - prefix[ch][c]

            # 2) For left window positions whose mirror is NOT in R:
            #    those i in M1 but outside [c..d] must match the fixed s[j].
            needL = [0]*26
            # segment1 = [m1_l .. min(m1_r, c-1)]
            s1, e1 = m1_l, min(m1_r, c-1)
            if s1 <= e1:
                for ch in range(26):
                    needL[ch] += prefix[ch][e1+1] - prefix[ch][s1]
            # segment2 = [max(m1_l, d+1) .. m1_r]
            s2, e2 = max(m1_l, d+1), m1_r
            if s2 <= e2:
                for ch in range(26):
                    needL[ch] += prefix[ch][e2+1] - prefix[ch][s2]

            # 3) For right window positions whose mirror is NOT in L:
            #    those j in M2 but outside [a..b] must match the fixed s[i].
            needR = [0]*26
            # segment1 = [m2_l .. min(m2_r, a-1)]
            s1, e1 = m2_l, min(m2_r, a-1)
            if s1 <= e1:
                for ch in range(26):
                    needR[ch] += prefix[ch][e1+1] - prefix[ch][s1]
            # segment2 = [max(m2_l, b+1) .. m2_r]
            s2, e2 = max(m2_l, b+1), m2_r
            if s2 <= e2:
                for ch in range(26):
                    needR[ch] += prefix[ch][e2+1] - prefix[ch][s2]

            # ----  Step C: Check resource feasibility and balance  ----
            #  * needL[ch] <= Lcnt[ch], needR[ch] <= Rcnt[ch]
            #  * after using up fixedâmatching chars, leftover multisets must be equal
            ok = True
            for ch in range(26):
                nl, nr = needL[ch], needR[ch]
                lm, rm = Lcnt[ch], Rcnt[ch]
                if nl > lm or nr > rm or (lm - nl) != (rm - nr):
                    ok = False
                    break

            ans.append(ok)

        return ans
