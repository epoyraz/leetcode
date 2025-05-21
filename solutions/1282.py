from collections import Counter

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        def to_mask(word):
            mask = 0
            for ch in set(word):  # set to avoid duplicates
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        # Step 1: Build frequency map of word bitmasks
        word_count = Counter(to_mask(word) for word in words if len(set(word)) <= 7)

        res = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            mask = to_mask(puzzle)
            sub = mask
            total = 0

            while sub:
                if sub & first:  # must include first letter
                    total += word_count.get(sub, 0)
                sub = (sub - 1) & mask  # next subset
            res.append(total)

        return res
