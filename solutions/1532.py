class Solution(object):
    def reformat(self, s):
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        res = []
        # Decide which type to start with (longer one goes first)
        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters

        for i in range(len(s)):
            if i % 2 == 0:
                res.append(first.pop())
            else:
                res.append(second.pop())

        return ''.join(res)
