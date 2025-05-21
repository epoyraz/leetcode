class Solution:
    def maxRepeating(self, sequence, word):
        k = 0
        t = word
        # Keep appending `word` until it's no longer a substring
        while t in sequence:
            k += 1
            t += word
        return k
