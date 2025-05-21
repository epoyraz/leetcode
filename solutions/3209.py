class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # dp[i] = minimum cost to cover fruits [0..i]
        dp = [float('inf')] * n
        
        for i in range(n):
            # any purchase at j covers up through index 2*j+1
            # we need j <= i and (2*j+1) >= i  => j >= ceil((i-1)/2)
            start_j = (i - 1 + 1) // 2  # ceil((i-1)/2)
            if start_j < 0:
                start_j = 0
            best = float('inf')
            for j in range(start_j, i + 1):
                prev = dp[j - 1] if j - 1 >= 0 else 0
                cost = prev + prices[j]
                if cost < best:
                    best = cost
            dp[i] = best
        
        return dp[n - 1]
