class Solution:
    def wordCount(self, startWords, targetWords):
        def to_mask(word):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        start_masks = set(to_mask(word) for word in startWords)
        res = 0

        for word in targetWords:
            mask = to_mask(word)
            for ch in word:
                prev_mask = mask ^ (1 << (ord(ch) - ord('a')))
                if prev_mask in start_masks:
                    res += 1
                    break

        return res
