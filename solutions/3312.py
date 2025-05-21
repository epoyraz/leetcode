class Solution(object):
    def countKeyChanges(self, s):
        cnt = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i-1].lower():
                cnt += 1
        return cnt
