class Solution(object):
    def maxProfit(self, prices):
        # initialize
        first_buy   = float('-inf')
        first_sell  = 0
        second_buy  = float('-inf')
        second_sell = 0

        for p in prices:
            # Maximize each state in turn
            first_buy   = max(first_buy,   -p)            # buy first share
            first_sell  = max(first_sell,  first_buy + p) # sell first share
            second_buy  = max(second_buy,  first_sell - p) # buy second share
            second_sell = max(second_sell, second_buy + p) # sell second share

        return second_sell
