class Solution(object):
    def checkValidGrid(self, grid):
        n = len(grid)
        total = n * n
        # record positions by move index
        pos = [None] * total
        for i in range(n):
            for j in range(n):
                idx = grid[i][j]
                pos[idx] = (i, j)
        # start at (0,0)
        if pos[0] != (0, 0):
            return False
        # knight moves
        for k in range(1, total):
            x1, y1 = pos[k-1]
            x2, y2 = pos[k]
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            if not ((dx == 1 and dy == 2) or (dx == 2 and dy == 1)):
                return False
        return True