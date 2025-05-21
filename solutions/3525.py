class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        Computes the maximum total energy boost over n hours when switching drinks incurs a 1-hour cleanse (zero boost).
        """
        n = len(energyDrinkA)
        # dpA: ending with A, dpB: ending with B, dpC: currently cleansing
        dpA = energyDrinkA[0]
        dpB = energyDrinkB[0]
        dpC = 0
        for i in range(1, n):
            a = energyDrinkA[i]
            b = energyDrinkB[i]
            # If we drink A now, we could have come from A or from cleansing
            newA = a + max(dpA, dpC)
            # If we drink B now, come from B or cleansing
            newB = b + max(dpB, dpC)
            # If we cleanse now, we skip boost, coming from any state
            newC = max(dpA, dpB, dpC)
            dpA, dpB, dpC = newA, newB, newC
        return max(dpA, dpB, dpC)