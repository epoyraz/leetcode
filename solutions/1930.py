class Solution(object):
    def getMaximumConsecutive(self, coins):
        coins.sort()
        max_reach = 0  # The maximum value we can make so far (inclusive)

        for coin in coins:
            if coin > max_reach + 1:
                break
            max_reach += coin

        return max_reach + 1  # Include 0
