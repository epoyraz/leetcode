class Solution(object):
    def secondHighest(self, s):
        digits = set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))
        if len(digits) < 2:
            return -1
        return sorted(digits, reverse=True)[1]
