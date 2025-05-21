from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        count = Counter(c.lower() for c in licensePlate if c.isalpha())
        res = None
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] >= count[c] for c in count):
                if res is None or len(word) < len(res):
                    res = word
        return res
