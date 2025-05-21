class Solution:
    def maxValue(self, n, x):
        s = str(n)
        c = str(x)
        if s[0] != '-':
            for i in range(len(s)):
                if s[i] < c:
                    return s[:i] + c + s[i:]
            return s + c
        for i in range(1, len(s)):
            if s[i] > c:
                return s[:i] + c + s[i:]
        return s + c
