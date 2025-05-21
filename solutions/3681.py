from itertools import combinations

class Solution(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pts = set((x, y) for x, y in points)
        n = len(points)
        best = 0
        
        # For each choice of 4 distinct points:
        for quad in combinations(points, 4):
            xs = sorted(p[0] for p in quad)
            ys = sorted(p[1] for p in quad)
            minx, maxx = xs[0], xs[-1]
            miny, maxy = ys[0], ys[-1]
            # Area must be positive
            if minx == maxx or miny == maxy:
                continue
            
            # Required corners
            corners = {
                (minx, miny),
                (minx, maxy),
                (maxx, miny),
                (maxx, maxy),
            }
            if set(map(tuple, quad)) != corners:
                continue
            
            # Check no other point lies inside or on the border
            ok = True
            for x, y in pts - corners:
                if minx <= x <= maxx and miny <= y <= maxy:
                    ok = False
                    break
            if not ok:
                continue
            
            # Valid rectangle
            area = (maxx - minx) * (maxy - miny)
            best = max(best, area)
        
        return best if best > 0 else -1
