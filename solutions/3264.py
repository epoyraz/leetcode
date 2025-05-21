class Solution(object):
    def maximumPoints(self, enemyEnergies, currentEnergy):
        """
        :type enemyEnergies: List[int]
        :type currentEnergy: int
        :rtype: int
        """
        # cheapest attackâcost
        f = min(enemyEnergies)
        # need at least one attack to unlock any rests
        if currentEnergy < f:
            return 0
        # leave one cheapest enemy unmarked so we can keep using it for attacks,
        # rest on all the others to pool their energy,
        # then do all possible attacks on the cheapest.
        total = sum(enemyEnergies)
        # formula derived: final points = floor((E0 + (sum_all - f)) / f)
        return (currentEnergy + total - f) // f
