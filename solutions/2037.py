import math

class Solution(object):
    def countTriples(self, n):
        count = 0
        for c in range(1, n+1):
            c2 = c*c
            for a in range(1, n+1):
                b2 = c2 - a*a
                if b2 <= 0:
                    continue
                b = int(math.sqrt(b2))
                if b*b == b2 and b <= n:
                    count += 1
        return count
