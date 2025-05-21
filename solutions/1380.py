class Solution:
    def closedIsland(self, grid):
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            grid[r][c] = 1
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r + dr, c + dc)

        # Eliminate all lands connected to the border
        for r in range(rows):
            for c in [0, cols - 1]:
                if grid[r][c] == 0:
                    dfs(r, c)
        for c in range(cols):
            for r in [0, rows - 1]:
                if grid[r][c] == 0:
                    dfs(r, c)

        # Count closed islands
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    closed_islands += 1

        return closed_islands
