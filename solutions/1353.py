class Solution:
    def removeAnagrams(self, words):
        res = []
        prev_sig = None
        for w in words:
            sig = ''.join(sorted(w))
            if sig != prev_sig:
                res.append(w)
                prev_sig = sig
        return res
