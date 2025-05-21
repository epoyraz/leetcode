class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # collect unique lowercase and uppercase letters
        lowers = set()
        uppers = set()
        for ch in word:
            if 'a' <= ch <= 'z':
                lowers.add(ch)
            elif 'A' <= ch <= 'Z':
                uppers.add(ch)
        # count characters whose lowercase form appears in both sets
        count = 0
        for c in lowers:
            if c.upper() in uppers:
                count += 1
        return count