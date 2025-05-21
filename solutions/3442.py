class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        # Only one copy of each value can ever be used
        arr = sorted(set(rewardValues))
        cap = arr[-1]           # we'll only track sums j < cap
        dp = [False] * cap      # dp[j] = True iff we can build a superincreasing
                                # subset of processed values summing exactly to j
        dp[0] = True
        ans = 0

        for v in arr:
            # 1) see what's the best prefixâsum we can get that is < v
            bestPrev = 0
            for j in range(v - 1, -1, -1):
                if dp[j]:
                    bestPrev = j
                    break
            # combining that prefix with v itself gives total v + bestPrev
            ans = max(ans, v + bestPrev)

            # 2) now incorporate v into our dp (for future values)
            #    we can only append v onto prefixes of sum j < v,
            #    and we only care about sums < cap
            #    so j must satisfy j <= min(v-1, cap-1-v)
            if v < cap:
                jMax = min(v - 1, cap - 1 - v)
                for j in range(jMax, -1, -1):
                    if dp[j]:
                        dp[j + v] = True

        return ans
