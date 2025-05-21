class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        def to_num(s):
            return int(''.join(str(ord(c) - ord('a')) for c in s))
        return to_num(firstWord) + to_num(secondWord) == to_num(targetWord)
