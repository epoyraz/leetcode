class Solution(object):
    def maxPossibleScore(self, start, d):
        # Build and sort intervals by their end = start + d
        intervals = sorted((s, s + d) for s in start)

        def feasible(M):
            # Can we pick one point per interval so that any two are â¥ M apart?
            # Greedy schedule: treat each interval as a job with window [s,e],
            # requiring separation M between chosen points.
            current = -M
            for s, e in intervals:
                # next point must be â¥ s and â¥ current + M
                p = current + M
                if p < s:
                    p = s
                # if it exceeds the interval end, fail
                if p > e:
                    return False
                current = p
            return True

        # Binary search max M
        lo, hi = 0, intervals[-1][1] - intervals[0][0]  # max possible span
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return best
