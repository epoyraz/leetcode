import collections

class Solution(object):
    def minimumPushes(self, word):
        freq = collections.Counter(word)
        freqs = sorted(freq.values(), reverse=True)

        total = 0
        pos = 0
        for f in freqs:
            total += (pos // 8 + 1) * f
            pos += 1
        return total
