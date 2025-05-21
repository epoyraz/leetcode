class Solution(object):
    def numberOfWays(self, s):
        n = len(s)
        p0 = [0] * (n + 1)
        p1 = [0] * (n + 1)
        for i in xrange(n):
            p0[i+1] = p0[i] + (s[i] == '0')
            p1[i+1] = p1[i] + (s[i] == '1')
        total0 = p0[n]
        total1 = p1[n]
        ans = 0
        for j in xrange(n):
            if s[j] == '1':
                zl = p0[j]
                zr = total0 - p0[j+1]
                ans += zl * zr
            else:
                ol = p1[j]
                or_ = total1 - p1[j+1]
                ans += ol * or_
        return ans
