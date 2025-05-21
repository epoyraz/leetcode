class Solution:
    def isRectangleCover(self, rectangles):
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        points = set()
        area = 0
        
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            area += (x2 - x1) * (y2 - y1)
            
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)
        
        if len(points) != 4 or (min_x, min_y) not in points or (min_x, max_y) not in points or (max_x, min_y) not in points or (max_x, max_y) not in points:
            return False
        
        return area == (max_x - min_x) * (max_y - min_y)
