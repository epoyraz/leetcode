class Solution(object):
    def projectionArea(self, grid):
        n = len(grid)
        xy = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        yz = sum(max(row) for row in grid)
        zx = sum(max(col) for col in zip(*grid))
        return xy + yz + zx
