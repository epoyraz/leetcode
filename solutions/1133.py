class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            else:
                j = j + k + 1
                k = 0
        return s[i:]
