class Solution:
    def finalString(self, s):
        res = []
        rev = False
        for c in s:
            if c == 'i':
                rev = not rev
            else:
                if rev:
                    res.insert(0, c)
                else:
                    res.append(c)
        return ''.join(res[::-1] if rev else res)
