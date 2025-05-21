class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []
        for word in words:
            w = set(word.lower())
            if w <= row1 or w <= row2 or w <= row3:
                res.append(word)
        return res
