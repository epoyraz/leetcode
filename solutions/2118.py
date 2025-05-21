class Solution:
    def maxTaxiEarnings(self, n, rides):
        from collections import defaultdict

        # Group rides by their end point
        end_at = defaultdict(list)
        for start, end, tip in rides:
            end_at[end].append((start, tip))

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # Option 1: skip taking a ride ending at i
            dp[i] = dp[i - 1]
            # Option 2: consider rides ending at i
            for start, tip in end_at[i]:
                dp[i] = max(dp[i], dp[start] + i - start + tip)

        return dp[n]
