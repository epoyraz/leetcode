from collections import defaultdict

class DetectSquares:
    def __init__(self):
        # count of each point (x,y)
        self.pointCount = defaultdict(int)
        # for each x, a map y -> count of points at (x,y)
        self.colPoints = defaultdict(lambda: defaultdict(int))

    def add(self, point):
        x, y = point
        self.pointCount[(x, y)] += 1
        self.colPoints[x][y] += 1

    def count(self, point):
        qx, qy = point
        res = 0
        # iterate over all points (qx, y) sharing x = qx
        colMap = self.colPoints[qx]
        for y, cnt_y in colMap.items():
            if y == qy:
                continue
            # side length of potential square
            d = y - qy
            # two candidate x-coordinates for the other corners
            for x in (qx + d, qx - d):
                cnt1 = self.pointCount.get((x, qy), 0)
                cnt2 = self.pointCount.get((x, y), 0)
                if cnt1 > 0 and cnt2 > 0:
                    # multiply counts for all combinations of duplicates
                    res += cnt_y * cnt1 * cnt2
        return res
