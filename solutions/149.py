class Solution(object):
    def maxPoints(self, points):
        import collections
        if not points:
            return 0
        n = len(points)
        res = 1
        for i in range(n):
            counter = collections.Counter()
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                gcd = self.gcd(dx, dy)
                if gcd != 0:
                    dx //= gcd
                    dy //= gcd
                counter[(dx, dy)] += 1
            if counter:
                res = max(res, max(counter.values()) + 1)
        return res

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
