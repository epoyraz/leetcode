class Solution(object):
    def maxPower(self, s):
        max_len = cur_len = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_len += 1
            else:
                cur_len = 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
