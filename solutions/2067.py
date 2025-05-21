class Solution(object):
    def maxPoints(self, points):
        m = len(points)
        n = len(points[0])
        dp = points[0][:]
        for r in range(1, m):
            newDp = [0]*n
            best = float("-inf")
            # left-to-right pass
            for c in range(n):
                best = max(best, dp[c] + c)
                newDp[c] = best - c + points[r][c]
            # right-to-left pass
            best = float("-inf")
            for c in range(n-1, -1, -1):
                best = max(best, dp[c] - c)
                newDp[c] = max(newDp[c], best + c + points[r][c])
            dp = newDp
        return max(dp)
