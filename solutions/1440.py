class Solution:
    def getNoZeroIntegers(self, n):
        def is_no_zero(x):
            while x:
                if x % 10 == 0:
                    return False
                x //= 10
            return True

        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]
        # problem guarantees a solution exists, so we should never get here
