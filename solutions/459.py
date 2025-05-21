class Solution:
    def repeatedSubstringPattern(self, s):
        return (s + s)[1:-1].find(s) != -1
