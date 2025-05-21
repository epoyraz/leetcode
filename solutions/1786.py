class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        return sum(all(c in allowed_set for c in word) for word in words)
