class Solution(object):
    def maxValueOfCoins(self, piles, k):
        # dp[j]: max value picking j coins so far
        dp = [-10**18] * (k + 1)
        dp[0] = 0
        for pile in piles:
            # compute prefix sums
            pre = [0]
            for v in pile:
                pre.append(pre[-1] + v)
            m = len(pile)
            # new dp for this pile
            ndp = dp[:]  # copy
            for j in xrange(k + 1):
                if dp[j] < 0:
                    continue
                # try taking x coins from this pile
                # x from 1 to min(m, k-j)
                up = min(m, k - j)
                for x in xrange(1, up + 1):
                    val = dp[j] + pre[x]
                    if val > ndp[j + x]:
                        ndp[j + x] = val
            dp = ndp
        return dp[k]
