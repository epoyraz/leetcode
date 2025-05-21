from collections import deque

class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]  # right, left, down, up

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        dq = deque()
        dq.append((0, 0))

        while dq:
            x, y = dq.popleft()
            for i, (dx, dy) in enumerate(dirs):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cost = 0 if grid[x][y] == i + 1 else 1
                    if dist[nx][ny] > dist[x][y] + cost:
                        dist[nx][ny] = dist[x][y] + cost
                        if cost == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        
        return dist[m - 1][n - 1]
