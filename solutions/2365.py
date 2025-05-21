class Solution:
    def percentageLetter(self, s, letter):
        count = s.count(letter)
        return (count * 100) // len(s)
