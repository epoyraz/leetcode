class Solution:
    def mincostTickets(self, days, costs):
        day_set = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        for d in range(1, last_day + 1):
            if d not in day_set:
                dp[d] = dp[d - 1]
            else:
                dp[d] = min(
                    dp[max(0, d - 1)] + costs[0],
                    dp[max(0, d - 7)] + costs[1],
                    dp[max(0, d - 30)] + costs[2],
                )

        return dp[last_day]
