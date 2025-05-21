class Solution(object):
    def onesMinusZeros(self, grid):
        m = len(grid)
        n = len(grid[0])
        onesRow = [sum(row) for row in grid]
        onesCol = [0] * n
        for row in grid:
            for j, v in enumerate(row):
                onesCol[j] += v
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = 2 * onesRow[i] + 2 * onesCol[j] - m - n
        return res
