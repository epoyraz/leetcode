class Solution(object):
    def largestMultipleOfThree(self, digits):
        digits.sort(reverse=True)
        total = sum(digits)
        mod1, mod2 = [], []

        for d in digits:
            if d % 3 == 1:
                mod1.append(d)
            elif d % 3 == 2:
                mod2.append(d)

        remainder = total % 3

        if remainder == 1:
            if mod1:
                digits.remove(min(mod1))
            elif len(mod2) >= 2:
                digits.remove(min(mod2))
                mod2.remove(min(mod2))
                digits.remove(min(mod2))
            else:
                return ""
        elif remainder == 2:
            if mod2:
                digits.remove(min(mod2))
            elif len(mod1) >= 2:
                digits.remove(min(mod1))
                mod1.remove(min(mod1))
                digits.remove(min(mod1))
            else:
                return ""

        if not digits:
            return ""
        if digits[0] == 0:
            return "0"

        digits.sort(reverse=True)
        return ''.join(map(str, digits))
