class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        shift_count = [0] * 26

        for i in range(len(s)):
            diff = (ord(t[i]) - ord(s[i])) % 26
            if diff == 0:
                continue
            times_needed = shift_count[diff]
            move = diff + 26 * times_needed
            if move > k:
                return False
            shift_count[diff] += 1

        return True
