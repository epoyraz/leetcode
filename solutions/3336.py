class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # total drunk starts with the initial full bottles
        total = numBottles
        # empty bottles after drinking them all
        empty = numBottles
        k = numExchange
        
        # as long as we have enough empties to do one exchange at the current rate
        while empty >= k:
            # perform exactly one exchange at this rate
            empty -= k
            # we get one new full bottle
            total += 1
            # after drinking it, we get one more empty
            empty += 1
            # rate increases by 1
            k += 1
        
        return total
