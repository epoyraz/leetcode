class Solution:
    def maxScore(self, s):
        max_score = 0
        for i in range(1, len(s)):
            left = s[:i].count('0')
            right = s[i:].count('1')
            max_score = max(max_score, left + right)
        return max_score
