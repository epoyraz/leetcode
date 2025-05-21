class Solution:
    def minAreaRect(self, points):
        point_set = set(map(tuple, points))
        min_area = float('inf')

        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # Must form a diagonal (not same row or column)
                if x1 != x2 and y1 != y2:
                    # Check if the other two corners exist
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(min_area, area)

        return 0 if min_area == float('inf') else min_area
