class Solution:
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        curr = capacity
        steps = 0
        
        for i, need in enumerate(plants):
            # If we donât have enough for this plant, go refill:
            if curr < need:
                # walk back from plant (i-1) to river and then out to plant i
                steps += 2 * i + 1
                curr = capacity
            else:
                # just walk one step from (i-1) to i
                steps += 1
            
            # water the plant
            curr -= need
        
        return steps
