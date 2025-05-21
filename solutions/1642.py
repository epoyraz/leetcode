class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = empty % numExchange + new_full

        return total
