import bisect

class Solution:
    def successfulPairs(self, spells, potions, success):
        # Sort the potions to allow binary search
        potions.sort()
        m = len(potions)
        result = []
        
        for s in spells:
            # Minimum potion strength needed so that s * p >= success
            # i.e. p >= ceil(success / s)
            need = (success + s - 1) // s
            # Find first index in potions with value >= need
            idx = bisect.bisect_left(potions, need)
            # All potions from idx..end will work
            result.append(m - idx)
        
        return result
