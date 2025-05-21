class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # cash: max profit if we do not hold a stock
        # hold: max profit if we hold a stock
        cash, hold = 0, -prices[0]
        
        for price in prices[1:]:
            # either keep cash, or sell the stock today and pay fee
            cash = max(cash, hold + price - fee)
            # either keep holding, or buy today with current cash
            hold = max(hold, cash - price)
        
        return cash
