class Solution(object):
    def isPrefixString(self, s, words):
        prefix = ""
        for w in words:
            prefix += w
            if prefix == s:
                return True
            if not s.startswith(prefix):
                return False
        return False
