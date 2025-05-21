class Solution:
    def sortSentence(self, s):
        words = s.split()
        res = [""] * len(words)
        for w in words:
            idx = int(w[-1]) - 1
            res[idx] = w[:-1]
        return " ".join(res)
