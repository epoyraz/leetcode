import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        dp = []
        for h in heights:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)
