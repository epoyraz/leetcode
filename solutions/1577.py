import math

class Solution(object):
    def getProbability(self, balls):
        """
        :type balls: List[int]
        :rtype: float
        """
        k = len(balls)
        half = sum(balls) // 2

        # simple comb implementation
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            num = den = 1
            for i in range(1, r + 1):
                num *= n - r + i
                den *= i
            return num // den

        def dfs(i, count, d1, d2):
            # returns (total_ways, favorable_ways)
            if i == k:
                if count == half:
                    return (1, 1) if d1 == d2 else (1, 0)
                return (0, 0)
            tot = fav = 0
            for x in range(balls[i] + 1):
                if count + x > half:
                    break
                w = comb(balls[i], x)
                t, f = dfs(
                    i + 1,
                    count + x,
                    d1 + (1 if x     > 0 else 0),
                    d2 + (1 if balls[i] - x > 0 else 0)
                )
                tot += w * t
                fav += w * f
            return tot, fav

        total, favorable = dfs(0, 0, 0, 0)
        # <-- force float division:
        return favorable / float(total)
