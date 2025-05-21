class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        
        for xstart, xend in points[1:]:
            if xstart > end:
                arrows += 1
                end = xend
        
        return arrows
