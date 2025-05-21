class Solution(object):
    def splitNum(self, num):
        digits = sorted(str(num))
        num1, num2 = '', ''
        for i, d in enumerate(digits):
            if i % 2 == 0:
                num1 += d
            else:
                num2 += d
        return int(num1) + int(num2)
