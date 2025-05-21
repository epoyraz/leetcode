import math

class Solution(object):
    def isThree(self, n):
        # Only perfect squares of a prime have exactly three divisors.
        m = int(math.sqrt(n))
        if m * m != n:
            return False
        if m < 2:
            return False
        # check primality of m
        r = int(math.sqrt(m))
        for d in range(2, r+1):
            if m % d == 0:
                return False
        return True
