class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Clamp the circle center to the rectangle boundaries
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate squared distance from the circle center to the closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        
        return dx * dx + dy * dy <= radius * radius
