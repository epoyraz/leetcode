from collections import Counter
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = Counter(deck).values()
        g = reduce(gcd, count)
        return g >= 2
