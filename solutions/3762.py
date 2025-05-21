class Solution(object):
    def maxScore(self, points, m):
        """
        :type points: List[int]
        :type m: int
        :rtype: int
        """
        n = len(points)

        def can(X):
            # how many visits we need at each i
            N = [(X + p - 1)//p for p in points]
            # L_prev = times we crossed into node 0 from -1
            L_prev = 1   # the very first move must be -1->0
            moves = 1    # that initial move

            # now for j=0..n-2 we choose R_j and L_j greedily
            # R_j = max(0, N[j] - L_prev)  (visits at j from the right)
            # must have R_j <= L_j  (can't cross back more than we crossed forward)
            # so we set L_j = max(R_j, N[j+1]) when j=n-2 (to serve last node),
            # otherwise L_j = R_j
            for j in xrange(n-1):
                # how many times must we come back from j+1->j?
                R = N[j] - L_prev
                if R < 0:
                    R = 0
                # how many times must we go forward j->j+1?
                if j == n-2:
                    # last edge must also deliver N[n-1] visits at node n-1
                    L = max(R, N[j+1])
                else:
                    L = R
                moves += R + L
                if moves > m:
                    return False
                L_prev = L

            return True

        # binary search for the largest X with can(X) == True
        lo, hi, ans = 0, m*max(points), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
