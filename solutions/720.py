class Solution(object):
    def longestWord(self, words):
        # Put all words into a set for O(1) lookups
        word_set = set(words)
        # Sort by descending length, then lexicographically ascending
        words.sort(key=lambda w: (-len(w), w))
        
        for w in words:
            # Check if every prefix of w exists
            valid = True
            for i in range(1, len(w)):
                if w[:i] not in word_set:
                    valid = False
                    break
            if valid:
                return w
        
        return ""
