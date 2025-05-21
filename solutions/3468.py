class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        k %= n
        return s[k:] + s[:k]
