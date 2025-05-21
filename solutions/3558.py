from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        visited = [[-1]*n for _ in range(m)]
        dq = deque()
        dq.append((0, 0, health - grid[0][0]))
        visited[0][0] = health - grid[0][0]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        while dq:
            x, y, h = dq.popleft()
            if h <= 0:
                continue
            if x == m - 1 and y == n - 1:
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh > visited[nx][ny]:
                        visited[nx][ny] = nh
                        dq.append((nx, ny, nh))
        return False
