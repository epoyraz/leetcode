class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # Sort box types by units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        remaining = truckSize
        
        for count, units in boxTypes:
            if remaining == 0:
                break
            # Take as many boxes of this type as we can
            take = min(count, remaining)
            total_units += take * units
            remaining -= take
        
        return total_units
