class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        left = 0
        count = 0

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                count += 1
            while count > 1:
                if s[left] == s[left + 1]:
                    count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max(max_len, 1)
