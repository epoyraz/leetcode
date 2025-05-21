class Solution:
    def sellingWood(self, m, n, prices):
        # price[h][w] = offered price for that exact rectangle (or 0 if none)
        price = [[0]*(n+1) for _ in range(m+1)]
        for h, w, p in prices:
            price[h][w] = p

        # dp[h][w] = max money from a hÃw rectangle
        dp = [[0]*(n+1) for _ in range(m+1)]

        for h in range(1, m+1):
            for w in range(1, n+1):
                # start with the price of the whole piece, if we can sell it
                best = price[h][w]

                # try all horizontal cuts
                for k in range(1, h//2 + 1):
                    best = max(best, dp[k][w] + dp[h - k][w])

                # try all vertical cuts
                for k in range(1, w//2 + 1):
                    best = max(best, dp[h][k] + dp[h][w - k])

                dp[h][w] = best

        return dp[m][n]
