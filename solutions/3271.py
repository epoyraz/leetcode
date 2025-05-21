class Solution(object):
    def countOfPairs(self, n, x, y):
        res = [0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                d1 = abs(i - j)
                d2 = abs(i - x) + 1 + abs(y - j)
                d3 = abs(i - y) + 1 + abs(x - j)
                d = min(d1, d2, d3)
                res[d - 1] += 1
        return res
