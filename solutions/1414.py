from collections import deque

class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2  # shortcut if we can go straight through

        visited = set()
        queue = deque([(0, 0, 0, 0)])  # (x, y, steps, obstacles_used)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            x, y, steps, obs = queue.popleft()

            if (x, y, obs) in visited:
                continue
            visited.add((x, y, obs))

            if x == m - 1 and y == n - 1:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_obs = obs + grid[nx][ny]
                    if new_obs <= k and (nx, ny, new_obs) not in visited:
                        queue.append((nx, ny, steps + 1, new_obs))

        return -1
