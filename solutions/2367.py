class Solution:
    def minimumLines(self, stockPrices):
        n = len(stockPrices)
        if n < 2:
            return 0
        
        # Sort by day (x-coordinate)
        stockPrices.sort()
        
        # Helper to get slope comparison without division:
        # returns True if slope between (x1,y1)->(x2,y2) equals slope between (x2,y2)->(x3,y3)
        def same_slope(x1, y1, x2, y2, x3, y3):
            return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
        
        # At least one line between the first two points
        lines = 1
        
        # Iterate through triples and count when slope changes
        for i in range(2, n):
            x1, y1 = stockPrices[i-2]
            x2, y2 = stockPrices[i-1]
            x3, y3 = stockPrices[i]
            
            if not same_slope(x1, y1, x2, y2, x3, y3):
                lines += 1
        
        return lines
