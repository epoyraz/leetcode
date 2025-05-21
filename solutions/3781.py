class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 1. Map to 1D and sort
        A = []
        for x,y in points:
            if y == 0:
                c = x
            elif x == side:
                c = side + y
            elif y == side:
                c = 2*side + (side - x)
            else:  # x == 0
                c = 3*side + (side - y)
            A.append(c)
        A.sort()

        # 2. Unroll: duplicate with +4*side
        P = A + [c + 4*side for c in A]
        n = len(A)

        # 3. Precompute next pointers for any d
        def build_next(d):
            nxt = [2*n] * (2*n)
            j = 0
            for i in range(2*n):
                if j < i+1:
                    j = i+1
                while j < 2*n and P[j] - P[i] < d:
                    j += 1
                nxt[i] = j
            return nxt

        # 4. Feasibility check with wrapâaround guard
        def can(d):
            nxt = build_next(d)
            for start in range(n):
                cur = start
                # pick k-1 subsequent points
                for _ in range(k-1):
                    cur = nxt[cur]
                    if cur >= start + n:
                        break
                else:
                    # we have indices start=i0 < i1 < ... < i_{k-1} < i+n
                    # now check the wrapâaround distance between last and first
                    i0 = start
                    ik = cur
                    gap1 = 4*side - (P[ik] - P[i0])      # wrap distance
                    # also direct across end-of-loop:
                    gap2 = P[start+n] - P[ik]
                    if min(gap1, gap2) >= d:
                        return True
            return False

        # 5. Binary search d in [0..2*side]
        lo, hi, ans = 0, 2*side, 0
        while lo <= hi:
            mid = (lo + hi)//2
            if mid == 0 or can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
