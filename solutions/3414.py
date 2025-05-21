class Solution(object):
    def waysToReachStair(self, k):
        """
        :type k: int
        :rtype: int
        """
        # Helper to compute binomial coefficient C(n, r)
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            # take advantage of symmetry
            r = min(r, n - r)
            res = 1
            for i in range(1, r+1):
                # multiply by (nâr+i) then divide by i,
                # doing integer arithmetic to stay exact
                res = res * (n - r + i) // i
            return res

        ans = 0
        U = 0
        # We try using U upwardâmoves in total.
        # They contribute sum_{j=0..Uâ1} 2^j = 2^Uâ1 upward steps,
        # and D downward moves subtracting 1 each.
        # Final position = 1 + (2^Uâ1) â D = 2^U â D must equal k,
        # so D = 2^U â k.  We only count it if 0 <= D <= U+1,
        # and choose positions for D nonâconsecutive downs among U+1 slots:
        # C(U+1, D).  Once 2^U â k > U+1, no larger U can work.
        while True:
            D = (1 << U) - k
            if D > U + 1:
                break
            if D >= 0:
                ans += comb(U + 1, D)
            U += 1

        return ans
