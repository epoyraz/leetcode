import math

class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # tetrahedral number T(k) = k(k+1)(k+2)/6
        def tetra(k):
            return k * (k + 1) * (k + 2) // 6

        # -------- 1. largest full staircase that fits ----------
        lo, hi = 0, 2 * int((6 * n) ** (1.0 / 3)) + 3   # safe upper bound on k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if tetra(mid) <= n:
                lo = mid
            else:
                hi = mid - 1
        k = lo                                    # height of the complete staircase
        used = tetra(k)
        base = k * (k + 1) // 2                   # floor boxes in those k layers
        rem = n - used                            # boxes still to place

        if rem == 0:
            return base

        # -------- 2. extra floor boxes for the leftover --------
        # solve add(add+1)/2 >= rem  ->  add = ceil( (sqrt(1+8*rem)-1)/2 )
        add = int(math.ceil((math.sqrt(1 + 8 * rem) - 1) / 2))
        return base + add
