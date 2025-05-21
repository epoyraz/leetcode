class Solution(object):
    def replaceDigits(self, s):
        res = list(s)
        for i in range(1, len(s), 2):
            res[i] = chr(ord(res[i-1]) + int(s[i]))
        return "".join(res)
