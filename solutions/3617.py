class Solution(object):
    def findAnswer(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[bool]
        """
        n = len(parent)
        # For the new problem: count possible original strings for final word
        # using at most one long-press event
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Compress the final word into groups of identical characters
        count = 1  # case with no long-press
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            f = j - i
            # if this group could be the long-pressed one (needs at least one extra char)
            if f >= 2:
                # intended group size can be from 1 to f-1
                count += f - 1
            i = j
        return count