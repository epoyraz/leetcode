import math

class Solution(object):
    def closestDivisors(self, num):
        def find_closest(n):
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]
            return []

        res1 = find_closest(num + 1)
        res2 = find_closest(num + 2)
        return res1 if abs(res1[0] - res1[1]) <= abs(res2[0] - res2[1]) else res2
