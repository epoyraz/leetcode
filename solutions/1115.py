class Solution:
    def isBoomerang(self, points):
        (x1, y1), (x2, y2), (x3, y3) = points
        # Check all points are distinct
        if len({(x1, y1), (x2, y2), (x3, y3)}) < 3:
            return False
        # Check not collinear via cross-product (area != 0)
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
