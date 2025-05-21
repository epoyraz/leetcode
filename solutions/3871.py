from collections import Counter

class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = Counter(s)
        distinct = len(freq)
        # If already â¤ k distinct characters, no deletions needed
        if distinct <= k:
            return 0
        
        # We need to remove (distinct - k) characters entirely.
        # To minimize deletions, pick the characters with the smallest frequencies.
        counts = sorted(freq.values())
        to_remove = distinct - k
        return sum(counts[:to_remove])
