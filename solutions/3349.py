class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict

        left = 0
        count = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # If any character count goes above 2, shrink the window from the left
            while any(v > 2 for v in count.values()):
                count[s[left]] -= 1
                left += 1

            # Update maximum length
            max_len = max(max_len, right - left + 1)

        return max_len
