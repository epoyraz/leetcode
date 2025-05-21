class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        size = n * 3
        expanded = [[0] * size for _ in range(size)]

        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                r, c3 = i * 3, j * 3
                if c == '/':
                    expanded[r][c3 + 2] = 1
                    expanded[r + 1][c3 + 1] = 1
                    expanded[r + 2][c3] = 1
                elif c == '\\':
                    expanded[r][c3] = 1
                    expanded[r + 1][c3 + 1] = 1
                    expanded[r + 2][c3 + 2] = 1

        def dfs(x, y):
            if x < 0 or y < 0 or x >= size or y >= size or expanded[x][y] != 0:
                return
            expanded[x][y] = 2
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        regions = 0
        for i in range(size):
            for j in range(size):
                if expanded[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions
