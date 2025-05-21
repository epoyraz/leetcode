class Solution(object):
    def longestPrefix(self, s):
        n = len(s)
        lps = [0] * n  # Longest Prefix Suffix array (KMP)

        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return s[:lps[-1]]
