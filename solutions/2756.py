class Solution:
    def buyChoco(self, prices, money):
        prices.sort()
        total = prices[0] + prices[1]
        return money - total if total <= money else money
