import math
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points):
        point_set = set(map(tuple, points))
        min_area = float('inf')
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]

                    # vectors
                    dx1, dy1 = x2 - x1, y2 - y1
                    dx2, dy2 = x3 - x1, y3 - y1

                    # check for right angle at point i (dot product == 0)
                    if dx1 * dx2 + dy1 * dy2 != 0:
                        continue

                    # compute the fourth point
                    x4, y4 = x3 + dx1, y3 + dy1

                    if (x4, y4) in point_set:
                        area = math.hypot(dx1, dy1) * math.hypot(dx2, dy2)
                        min_area = min(min_area, area)

        return 0 if min_area == float('inf') else min_area
