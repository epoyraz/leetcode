class Solution:
    def findSubstringInWraproundString(self, s):
        max_len = [0] * 26  # max length of substrings ending with each letter
        k = 0  # current length of valid substring

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            index = ord(s[i]) - ord('a')
            max_len[index] = max(max_len[index], k)

        return sum(max_len)
