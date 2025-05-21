import math

class Solution:
    def bestCoordinate(self, towers, radius):
        # Precompute radius squared
        r2 = radius * radius
        
        # Find bounds for search
        max_x = max(x for x, y, q in towers)
        max_y = max(y for x, y, q in towers)
        
        best_q = -1
        best_x = 0
        best_y = 0
        
        # Scan all non-negative integer coords within [0..max_x+radius] x [0..max_y+radius]
        for x in range(max_x + radius + 1):
            for y in range(max_y + radius + 1):
                total = 0
                # Sum contributions from each tower
                for tx, ty, tq in towers:
                    dx = tx - x
                    dy = ty - y
                    d2 = dx*dx + dy*dy
                    if d2 <= r2:
                        d = math.sqrt(d2)
                        total += int(tq / (1 + d))
                # Update best if we found a strictly larger quality,
                # or same quality but lexicographically smaller coordinate
                if total > best_q or (total == best_q and (x < best_x or (x == best_x and y < best_y))):
                    best_q = total
                    best_x = x
                    best_y = y
        
        return [best_x, best_y]
