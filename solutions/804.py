class Solution(object):
    def rotatedDigits(self, n):
        valid = {0, 1, 2, 5, 6, 8, 9}
        diff = {2, 5, 6, 9}
        count = 0
        for num in range(1, n+1):
            digits = set(int(d) for d in str(num))
            if digits.issubset(valid) and digits & diff:
                count += 1
        return count
