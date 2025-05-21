class NeighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid
        self.n = len(grid)
        # Build a map from value â (row, col)
        self.pos = {}
        for i in range(self.n):
            for j in range(self.n):
                self.pos[grid[i][j]] = (i, j)

    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        i, j = self.pos[value]
        total = 0
        # up, down, left, right
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total += self.grid[ni][nj]
        return total

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        i, j = self.pos[value]
        total = 0
        # top-left, top-right, bottom-left, bottom-right
        for di, dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total += self.grid[ni][nj]
        return total
