class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        # Number of length-k blocks
        B = n // k
        
        # Count how many times each block appears
        freq = {}
        for i in range(0, n, k):
            block = word[i:i+k]
            freq[block] = freq.get(block, 0) + 1
        
        # We can only copy one of the existing blocks to all others.
        # Pick the block with maximum frequency (M),
        # then replace the other B - M blocks.
        max_count = max(freq.values())
        return B - max_count
