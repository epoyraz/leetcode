class Solution:
    def similarPairs(self, words):
        from collections import Counter
        masks = Counter()

        for word in words:
            mask = 0
            for ch in set(word):
                mask |= 1 << (ord(ch) - ord('a'))
            masks[mask] += 1

        count = 0
        for v in masks.values():
            count += v * (v - 1) // 2
        return count
