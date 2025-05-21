class Solution:
    def sequentialDigits(self, low, high):
        result = []
        digits = "123456789"

        for length in range(2, 10):  # Length of sequential number from 2 to 9
            for start in range(0, 10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)

        return result
