from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        for i in points:
            count = defaultdict(int)
            for j in points:
                dist = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                count[dist] += 1
            for c in count.values():
                res += c * (c - 1)
        return res
