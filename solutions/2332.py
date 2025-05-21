class Solution:
    def countLatticePoints(self, circles):
        # Since 1 <= xi, yi <= 100 and ri <= min(xi, yi),
        # all lattice points lie in [0..200] Ã [0..200].
        MAXC = 200
        # grid[x][y] = True if (x,y) is in at least one circle
        grid = [[False] * (MAXC+1) for _ in range(MAXC+1)]
        
        for xi, yi, ri in circles:
            r2 = ri * ri
            # sweep x from xi - ri to xi + ri
            x_lo = max(0, xi - ri)
            x_hi = min(MAXC, xi + ri)
            for x in range(x_lo, x_hi+1):
                dx = x - xi
                rem = r2 - dx*dx
                # largest integer dy with dy^2 <= rem
                dy = int(rem**0.5)
                y_lo = max(0, yi - dy)
                y_hi = min(MAXC, yi + dy)
                row = grid[x]
                for y in range(y_lo, y_hi+1):
                    row[y] = True
        
        # count marked points
        ans = 0
        for x in range(MAXC+1):
            ans += sum(grid[x])
        return ans
