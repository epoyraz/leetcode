class Solution:
    def alternateDigitSum(self, n):
        s = str(n)
        total = 0
        for i, ch in enumerate(s):
            digit = int(ch)
            if i % 2 == 0:
                total += digit
            else:
                total -= digit
        return total
