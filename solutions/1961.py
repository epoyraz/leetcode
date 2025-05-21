class Solution(object):
    def maxIceCream(self, costs, coins):
        # counting sort histogram
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1

        bars = 0
        for price in range(1, max_cost + 1):
            if coins < price:
                break
            count = freq[price]
            # buy as many as possible at this price
            can_buy = min(count, coins // price)
            bars += can_buy
            coins -= can_buy * price
        return bars
