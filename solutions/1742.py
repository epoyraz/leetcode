class Solution:
    def maxWidthOfVerticalArea(self, points):
        # Extract all x-coordinates
        xs = [x for x, _ in points]
        xs.sort()
        
        # Compute the maximum gap between consecutive x's
        max_gap = 0
        for i in range(1, len(xs)):
            gap = xs[i] - xs[i-1]
            if gap > max_gap:
                max_gap = gap
        
        return max_gap
