class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        pattern = "abc"
        p = 0
        inserts = 0
        
        for ch in word:
            # Insert missing pattern chars until we match ch
            while pattern[p] != ch:
                inserts += 1
                p = (p + 1) % 3
            # Consume ch
            p = (p + 1) % 3
        
        # After processing word, finish the current "abc" cycle
        if p != 0:
            inserts += (3 - p)
        
        return inserts
