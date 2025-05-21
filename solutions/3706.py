class Solution(object):
    def minLength(self, s, numOps):
        """
        :type s: str
        :type numOps: int
        :rtype: int
        """
        n = len(s)

        # ----- helpers -------------------------------------------------- #
        def flips_L1():
            """minimum flips to make the string strictly alternating"""
            d0 = d1 = 0            # 0101..., 1010...
            for i, ch in enumerate(s):
                if ch != ('0' if i & 1 == 0 else '1'):
                    d0 += 1
                if ch != ('1' if i & 1 == 0 else '0'):
                    d1 += 1
            return min(d0, d1)

        def flips_needed(L):
            if L == 1:
                return flips_L1()

            flips = 0
            run_len = 1
            for i in range(1, n):
                if s[i] == s[i - 1]:
                    run_len += 1
                else:
                    flips += run_len // (L + 1)
                    run_len = 1
            flips += run_len // (L + 1)       # last run
            return flips
        # ---------------------------------------------------------------- #

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if flips_needed(mid) <= numOps:   # feasible â try smaller L
                hi = mid
            else:
                lo = mid + 1                  # infeasible â need larger L
        return lo
