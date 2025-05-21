class Solution:
    def findTheDifference(self, s, t):
        res = 0
        for c in s + t:
            res ^= ord(c)
        return chr(res)
