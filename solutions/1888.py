class Solution:
    def nearestValidPoint(self, x, y, points):
        min_dist = float('inf')
        index = -1

        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                dist = abs(x - a) + abs(y - b)
                if dist < min_dist:
                    min_dist = dist
                    index = i

        return index
