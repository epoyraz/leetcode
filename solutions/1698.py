class Solution(object):
    def modifyString(self, s):
        res = list(s)
        n = len(res)
        for i in range(n):
            if res[i] == '?':
                for c in 'abc':
                    if (i > 0 and res[i-1] == c) or (i+1 < n and res[i+1] == c):
                        continue
                    res[i] = c
                    break
        return ''.join(res)
