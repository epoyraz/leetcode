class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = s
        n = len(s)
        for i in xrange(n-1):
            if (ord(s[i]) - ord('0')) % 2 == (ord(s[i+1]) - ord('0')) % 2:
                t = s[:i] + s[i+1] + s[i] + s[i+2:]
                if t < best:
                    best = t
        return best
