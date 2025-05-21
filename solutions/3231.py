class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        coins.sort()
        miss = 1
        i = 0
        patches = 0
        n = len(coins)

        # We maintain that all sums in [1..miss-1] are covered.
        # While we still need to cover up to 'target'...
        while miss <= target:
            # If the next coin extends coverage, use it.
            if i < n and coins[i] <= miss:
                miss += coins[i]
                i += 1
            else:
                # Otherwise, patch by adding 'miss' itself.
                miss += miss
                patches += 1

        return patches
