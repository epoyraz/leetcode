class Solution(object):
    def makeSmallestPalindrome(self, s):
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if s[i] < s[j]:
                    s[j] = s[i]
                else:
                    s[i] = s[j]
            i += 1
            j -= 1
        return ''.join(s)
