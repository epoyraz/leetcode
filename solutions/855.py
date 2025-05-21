class Solution(object):
    def uniqueLetterString(self, s):
        index = {}
        for i, c in enumerate(s):
            if c not in index:
                index[c] = []
            index[c].append(i)
        
        res = 0
        n = len(s)
        for idxs in index.values():
            for i, j in enumerate(idxs):
                prev = idxs[i-1] if i > 0 else -1
                nex = idxs[i+1] if i+1 < len(idxs) else n
                res += (j - prev) * (nex - j)
        return res
