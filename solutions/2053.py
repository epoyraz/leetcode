class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-97] += 1
        counts = [f for f in freq if f>0]
        return len(set(counts)) == 1
