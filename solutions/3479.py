class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # 1) substrings of all '1's
        ans = 0
        run = 0
        for ch in s:
            if ch == '1':
                run += 1
            else:
                ans += run * (run + 1) // 2
                run = 0
        ans += run * (run + 1) // 2

        # 2) zero positions
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        Z = len(zeros)
        if Z == 0:
            return ans

        # 3) max z with z(z+1) <= n, via float sqrt
        import math
        zmax = int((math.sqrt(1 + 4*n) - 1) // 2)

        # 4) slide window over zeros for each z
        for z in range(1, min(Z, zmax) + 1):
            M = z*(z+1)       # need substringâlength â¥ M â r-l+1 â¥ M â r-l â¥ M-1
            for k in range(Z - z + 1):
                left0 = zeros[k]
                right0 = zeros[k+z-1]
                A = zeros[k-1] + 1 if k > 0 else 0
                B = zeros[k+z] - 1 if (k+z) < Z else n - 1
                Rcount = B - right0 + 1
                if Rcount <= 0:
                    continue

                # Case 1: l â¤ right0-(M-1)
                t = right0 - (M - 1)
                L2 = min(left0, t)
                cnt = 0
                if L2 >= A:
                    cnt += (L2 - A + 1) * Rcount

                # Case 2: l > t, and r â¥ l+(M-1)
                start2 = max(A, t+1)
                # r runs from (l+M-1) to B, so count_r = B-(l+M-1)+1 = (B-M+2)-l = K-l
                K = B - M + 2
                U = min(left0, K - 1)
                if U >= start2:
                    c = U - start2 + 1
                    cnt += c*K - (start2 + U)*c//2

                ans += cnt

        return ans
