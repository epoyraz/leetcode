class Solution:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()
