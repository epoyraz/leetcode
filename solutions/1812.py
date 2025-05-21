class Solution(object):
    def reformatNumber(self, number):
        # remove non-digit characters
        digits = [c for c in number if c.isdigit()]
        res = []
        i, n = 0, len(digits)
        # take blocks of 3 while more than 4 remain
        while n - i > 4:
            res.append(''.join(digits[i:i+3]))
            i += 3
        # handle the last 4 or fewer digits
        rem = n - i
        if rem == 4:
            res.append(''.join(digits[i:i+2]))
            res.append(''.join(digits[i+2:i+4]))
        else:
            res.append(''.join(digits[i:]))
        return '-'.join(res)
