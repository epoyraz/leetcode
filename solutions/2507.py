import math

class Solution(object):
    def commonFactors(self, a, b):
        # Compute GCD with a simple loop (math.gcd may not be available)
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        g = gcd(a, b)
        # Count divisors of g
        cnt = 0
        root = int(g**0.5)
        for i in range(1, root + 1):
            if g % i == 0:
                cnt += 1
                if i != g // i:
                    cnt += 1
        return cnt
