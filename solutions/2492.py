class Solution:
    def longestContinuousSubstring(self, s):
        ans = curr = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                curr += 1
            else:
                curr = 1
            if curr > ans:
                ans = curr
        return ans
