class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight:   List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_side = 0
        
        for i in range(n):
            x1_i, y1_i = bottomLeft[i]
            x2_i, y2_i = topRight[i]
            for j in range(i+1, n):
                x1_j, y1_j = bottomLeft[j]
                x2_j, y2_j = topRight[j]
                
                # intersection coords
                x_left   = max(x1_i, x1_j)
                y_bottom = max(y1_i, y1_j)
                x_right  = min(x2_i, x2_j)
                y_top    = min(y2_i, y2_j)
                
                w = x_right - x_left
                h = y_top   - y_bottom
                if w > 0 and h > 0:
                    max_side = max(max_side, min(w, h))
        
        return max_side * max_side
