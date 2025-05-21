class Solution:
    def makeIntegerBeautiful(self, n, target):
        # Helper to compute digit sum
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        # If already beautiful, no need to add
        if digit_sum(n) <= target:
            return 0

        res = 0
        p = 1  # current power of ten
        # We'll zero out digits from least significant upward
        while digit_sum(n) > target:
            digit = (n // p) % 10
            inc = (10 - digit) % 10
            add = inc * p
            res += add
            n += add
            # Move to next digit
            p *= 10

        return res
