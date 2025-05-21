class Solution(object):
    def maximizeTheProfit(self, n, offers):
        from collections import defaultdict
        offers_by_end = defaultdict(list)
        
        for start, end, gold in offers:
            offers_by_end[end].append((start, gold))
        
        dp = [0] * (n + 1)  # dp[i]: max gold using houses [0..i-1]
        
        for i in range(1, n + 1):
            # Option 1: don't take any offer ending at i-1
            dp[i] = dp[i - 1]
            # Option 2: take one of the offers ending at i-1
            for start, gold in offers_by_end[i - 1]:
                dp[i] = max(dp[i], dp[start] + gold)
        
        return dp[n]
