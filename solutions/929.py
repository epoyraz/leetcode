class Solution(object):
    def numSpecialEquivGroups(self, words):
        seen = set()
        for word in words:
            even = sorted(word[::2])
            odd = sorted(word[1::2])
            seen.add((tuple(even), tuple(odd)))
        return len(seen)
