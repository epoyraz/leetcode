class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        i = 0
        while i < n:
            # evaluate block s[i] and s[i+1]
            if s[i] != s[i+1]:
                res += 1  # need 1 change to make the pair same
            i += 2
        return res
