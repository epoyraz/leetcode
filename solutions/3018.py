class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        j = 0
        m = len(str2)
        for c in str1:
            if j < m:
                # compute next character cyclically
                nc = 'a' if c == 'z' else chr(ord(c) + 1)
                if c == str2[j] or nc == str2[j]:
                    j += 1
        return j == m
