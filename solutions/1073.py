from collections import deque

class Solution:
    def numEnclaves(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque()
        # enqueue all boundary land cells
        for i in range(m):
            for j in (0, n - 1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        for j in range(n):
            for i in (0, m - 1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        # BFS to erase all land reachable from boundary
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
        # count remaining land
        cnt = 0
        for row in grid:
            cnt += sum(row)
        return cnt
