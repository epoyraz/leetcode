class Solution:
    def minTimeToVisitAllPoints(self, points):
        time = 0
        for i in range(1, len(points)):
            x0, y0 = points[i - 1]
            x1, y1 = points[i]
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            time += max(dx, dy)
        return time
