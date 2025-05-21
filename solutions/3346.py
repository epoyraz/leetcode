class Solution(object):
    def getSmallestString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def dist(a, b):
            # cyclic distance on 26âletter ring
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)
        
        rem = k
        res = []
        for ch in s:
            # try letters from 'a' to 'z'
            for c in map(chr, range(ord('a'), ord('z')+1)):
                d = dist(ch, c)
                if d <= rem:
                    res.append(c)
                    rem -= d
                    break
        return ''.join(res)
