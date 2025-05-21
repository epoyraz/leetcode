class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        # Compute how many more rocks each bag needs to be full
        needed = [c - r for c, r in zip(capacity, rocks)]
        # Fill the bags that need the fewest rocks first
        needed.sort()
        
        full = 0
        for n in needed:
            if n == 0:
                # Already full
                full += 1
            elif additionalRocks >= n:
                additionalRocks -= n
                full += 1
            else:
                break
        
        return full
