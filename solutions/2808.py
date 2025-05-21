class Solution:
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        n = len(cost)
        # Each paid wall i contributes (time[i] + 1) "workâunits"
        # We need total work â¥ n to cover the n freeâpainter slots.
        target = n
        # dp[w] = minimum money to achieve exactly w workâunits (clamped at target)
        INF = 10**30
        dp = [INF] * (target + 1)
        dp[0] = 0

        for c, t in zip(cost, time):
            w = t + 1
            # traverse backwards so 0-1 knapsack
            for curr in range(target, -1, -1):
                if dp[curr] == INF:
                    continue
                nxt = curr + w
                if nxt >= target:
                    nxt = target
                # either take wall i for paid painter
                if dp[nxt] > dp[curr] + c:
                    dp[nxt] = dp[curr] + c

        return dp[target]
