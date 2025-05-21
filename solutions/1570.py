class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        result = prices[:]

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    result[i] -= prices[j]
                    break

        return result
