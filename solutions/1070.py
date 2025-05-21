class Solution:
    def baseNeg2(self, n):
        if n == 0:
            return "0"
        digits = []
        while n != 0:
            n, rem = divmod(n, -2)
            if rem < 0:
                rem += 2
                n += 1
            digits.append(str(rem))
        return ''.join(reversed(digits))
