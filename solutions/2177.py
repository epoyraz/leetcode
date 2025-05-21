from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1, word2):
        """
        :param word1: str
        :param word2: str
        :return: bool  # True if for every letter 'a'â'z', |freq1 - freq2| â¤ 3
        """
        c1 = Counter(word1)
        c2 = Counter(word2)
        # Check each lowercase letter
        for ch in map(chr, range(ord('a'), ord('z')+1)):
            if abs(c1[ch] - c2[ch]) > 3:
                return False
        return True
