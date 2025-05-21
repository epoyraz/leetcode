class Solution:
    def minDeletions(self, s):
        from collections import Counter
        
        freq_counts = list(Counter(s).values())
        freq_counts.sort(reverse=True)
        
        used = set()
        deletions = 0
        
        for f in freq_counts:
            # Decrease f until it's unique (or zero)
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            if f > 0:
                used.add(f)
        
        return deletions
