from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        window_count = {}
        have, need = 0, len(t_count)
        res = [-1, -1]
        res_len = float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window_count[c] = window_count.get(c, 0) + 1

            if c in t_count and window_count[c] == t_count[c]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
