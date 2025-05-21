class Solution:
    def circularPermutation(self, n, start):
        res = []
        for i in range(1 << n):
            res.append(start ^ (i ^ (i >> 1)))
        return res
