class Solution(object):
    def makeFancyString(self, s):
        res = []
        prev = ''
        count = 0
        for c in s:
            if c == prev:
                count += 1
            else:
                prev = c
                count = 1
            if count <= 2:
                res.append(c)
        return "".join(res)
