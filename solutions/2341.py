class Solution:
    def countPrefixes(self, words, s):
        count = 0
        for w in words:
            if s.startswith(w):
                count += 1
        return count
