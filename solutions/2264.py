class Solution:
    def minimumSum(self, num):
        digits = sorted(map(int, str(num)))
        new1 = digits[0] * 10 + digits[2]
        new2 = digits[1] * 10 + digits[3]
        return new1 + new2
