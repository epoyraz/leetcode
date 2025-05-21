class Solution:
    def closeStrings(self, word1, word2):
        # If lengths differ, can't be close
        if len(word1) != len(word2):
            return False
        
        # Count frequencies
        from collections import Counter
        f1 = Counter(word1)
        f2 = Counter(word2)
        
        # Must have the same set of unique characters
        if set(f1.keys()) != set(f2.keys()):
            return False
        
        # The multiset of frequencies must match
        if sorted(f1.values()) != sorted(f2.values()):
            return False
        
        return True
