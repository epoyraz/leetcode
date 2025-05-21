class Solution:
    def countPyramids(self, grid):
        m, n = len(grid), len(grid[0])
        dp_down = [[0]*n for _ in range(m)]
        dp_up = [[0]*n for _ in range(m)]
        
        # Downward pyramids
        for r in range(m-2, -1, -1):
            for c in range(1, n-1):
                if grid[r][c] == 1 and grid[r+1][c-1] and grid[r+1][c] and grid[r+1][c+1]:
                    dp_down[r][c] = 1 + min(
                        dp_down[r+1][c-1],
                        dp_down[r+1][c],
                        dp_down[r+1][c+1]
                    )
        
        # Upward pyramids
        for r in range(1, m):
            for c in range(1, n-1):
                if grid[r][c] == 1 and grid[r-1][c-1] and grid[r-1][c] and grid[r-1][c+1]:
                    dp_up[r][c] = 1 + min(
                        dp_up[r-1][c-1],
                        dp_up[r-1][c],
                        dp_up[r-1][c+1]
                    )
        
        total = 0
        for r in range(m):
            for c in range(n):
                total += dp_down[r][c] + dp_up[r][c]
        return total
