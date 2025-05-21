from bisect import bisect_right

class Solution(object):
    def maxValue(self, events, k):
        events.sort()
        starts = [e[0] for e in events]
        n = len(events)
        memo = {}

        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Option 1: Skip this event
            skip = dp(i + 1, remaining)

            # Option 2: Take this event
            _, end, val = events[i]
            next_i = bisect_right(starts, end)
            take = val + dp(next_i, remaining - 1)

            memo[(i, remaining)] = max(skip, take)
            return memo[(i, remaining)]

        return dp(0, k)
