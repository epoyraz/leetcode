class Solution(object):
    def minimumCost(self, nums, cost, k):
        """
        :type nums: List[int]
        :type cost: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque

        n = len(nums)
        # prefix sums
        Pnum = [0]*n
        Pcost = [0]*n
        s1 = s2 = 0
        for i in range(n):
            s1 += nums[i]
            s2 += cost[i]
            Pnum[i] = s1
            Pcost[i] = s2

        INF = float('inf')
        # dpPrev[r] = best cost partitioning [0..r] into t-1 subarrays
        dpPrev = [INF]*n
        for r in range(n):
            dpPrev[r] = (Pnum[r] + k) * Pcost[r]
        ans = dpPrev[-1]

        def add_line(hull, m, b):
            # remove last while new line (m,b) makes it obsolete
            # lines in hull: ... (m1,b1), (m2,b2)
            # new is (m3,b3) = (m,b)
            # if (b2-b1)/(m1-m2) >= (b3-b2)/(m2-m3) then pop (m2,b2)
            while len(hull) >= 2:
                m1, b1 = hull[-2]
                m2, b2 = hull[-1]
                # correct check:
                if (b2 - b1) * (m2 - m) >= (b - b2) * (m1 - m2):
                    hull.pop()
                else:
                    break
            hull.append((m, b))

        def query(hull, x):
            # lines sorted by decreasing slope, x queries increasing
            while len(hull) >= 2 and hull[0][0]*x + hull[0][1] >= hull[1][0]*x + hull[1][1]:
                hull.popleft()
            m, b = hull[0]
            return m*x + b

        # build up number of subarrays t = 2..n
        for t in range(2, n+1):
            hull = deque()
            dpCurr = [INF]*n
            for r in range(t-1, n):
                # candidate from splitting before r:
                l = r-1
                add_line(hull, -Pcost[l], dpPrev[l])

                x = Pnum[r] + k*t
                best = query(hull, x)
                dpCurr[r] = x * Pcost[r] + best

            dpPrev = dpCurr
            ans = min(ans, dpPrev[-1])

        return ans
