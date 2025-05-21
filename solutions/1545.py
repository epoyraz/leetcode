class Solution(object):
    def largestNumber(self, cost, target):
        # dp[t] = max number of digits achievable with total cost t
        dp = [-10**9] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            for d, c in enumerate(cost, 1):
                if t >= c:
                    dp[t] = max(dp[t], dp[t - c] + 1)
        # if we can't form any digit, return "0"
        if dp[target] < 1:
            return "0"
        # reconstruct the largest number greedily
        res = []
        t = target
        for _ in range(dp[target]):
            for d in range(9, 0, -1):
                c = cost[d - 1]
                if t >= c and dp[t - c] == dp[t] - 1:
                    res.append(str(d))
                    t -= c
                    break
        return "".join(res)
