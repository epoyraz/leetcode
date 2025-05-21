from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        # Sort the deck in ascending order
        deck.sort()
        
        dq = deque()
        # Build the initial deck order in reverse
        for card in reversed(deck):
            if dq:
                # Reverse the "reveal then move top to bottom" step:
                # take the last element and move it to the front
                dq.appendleft(dq.pop())
            # Place the next largest card at the front
            dq.appendleft(card)
        
        return list(dq)
