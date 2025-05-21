class Solution:
    def bestHand(self, ranks, suits):
        # Check for Flush: all suits the same
        first_suit = suits[0]
        if all(s == first_suit for s in suits):
            return "Flush"
        
        # Count ranks
        count = {}
        for r in ranks:
            count[r] = count.get(r, 0) + 1
        
        # Three of a Kind?
        if any(c >= 3 for c in count.values()):
            return "Three of a Kind"
        
        # Pair?
        if any(c >= 2 for c in count.values()):
            return "Pair"
        
        # Otherwise
        return "High Card"
