class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        flips = 0
        current = '0'
        
        for bit in target:
            if bit != current:
                flips += 1
                current = bit  # flip toggles the current state
        
        return flips
