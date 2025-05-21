class Solution(object):
    def divisibilityArray(self, word, m):
        res = []
        curr = 0
        for ch in word:
            curr = (curr * 10 + int(ch)) % m
            res.append(1 if curr == 0 else 0)
        return res
