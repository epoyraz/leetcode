class Solution:
    def printVertically(self, s):
        words = s.split()
        max_len = max(len(w) for w in words)
        res = []
        for j in range(max_len):
            col = ''.join(w[j] if j < len(w) else ' ' for w in words)
            res.append(col.rstrip())
        return res
