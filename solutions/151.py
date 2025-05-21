class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])
