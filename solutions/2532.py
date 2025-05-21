from collections import Counter

class Solution(object):
    def equalFrequency(self, word):
        # Count how many times each letter appears
        letter_freq = Counter(word)
        # Build a histogram of those frequencies
        cnt = Counter(letter_freq.values())
        
        # If there's only one frequency overall:
        if len(cnt) == 1:
            # Extract the single (frequency, how_many_letters) pair
            for f, how_many in cnt.items():
                break
            # If that frequency is 1 (all letters unique), or there's only one letter type,
            # removing one occurrence still leaves a uniform frequency among remaining letters.
            if f == 1 or how_many == 1:
                return True
            else:
                return False
        
        # If there are exactly two distinct frequencies
        if len(cnt) == 2:
            (f1, c1), (f2, c2) = sorted(cnt.items())
            # Case A: one letter appears once, all others appear f2 times
            if f1 == 1 and c1 == 1:
                return True
            # Case B: one letter appears (f1+1) times and all others appear f1 times
            if f2 == f1 + 1 and c2 == 1:
                return True
        
        # In all other cases, it's impossible
        return False
