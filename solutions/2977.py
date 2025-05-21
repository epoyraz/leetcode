class Solution(object):
    def isAcronym(self, words, s):
        if len(words) != len(s):
            return False
        for i in range(len(words)):
            if words[i][0] != s[i]:
                return False
        return True
