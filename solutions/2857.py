class Solution:
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        used = 0
        # Each time we consume 5 L from main, we get 1 L from additional (if available)
        while mainTank >= 5 and additionalTank > 0:
            mainTank -= 5
            used += 5
            additionalTank -= 1
            mainTank += 1
        
        # consume whatever remains in the main tank
        used += mainTank
        
        # mileage is 10 km per liter
        return used * 10
