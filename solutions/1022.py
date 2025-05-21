class Solution:
    def uniquePathsIII(self, grid):
        rows, cols = len(grid), len(grid[0])
        empty = 0
        start_x = start_y = 0

        # Find the start and count non-obstacle squares
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                if grid[i][j] != -1:
                    empty += 1

        self.result = 0

        def dfs(x, y, remain):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                if remain == 1:
                    self.result += 1
                return

            temp = grid[x][y]
            grid[x][y] = -1  # mark visited
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(x + dx, y + dy, remain - 1)
            grid[x][y] = temp  # backtrack

        dfs(start_x, start_y, empty)
        return self.result
