from collections import deque

class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = [[0]*n for _ in range(n)]
        queue = deque()

        # DFS to mark the first island and collect its border
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = 1
            queue.append((x, y, 0))  # enqueue with step count
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        # Find first island and start DFS
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # BFS to expand to the second island
        while queue:
            x, y, d = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] == 1:
                        return d  # reached second island
                    visited[nx][ny] = 1
                    queue.append((nx, ny, d + 1))

        return -1  # Should never be reached
