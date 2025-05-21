from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        q = deque()

        # Add all land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        # If there's no land or no water, return -1
        if len(q) == 0 or len(q) == n * n:
            return -1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        distance = -1

        # Multi-source BFS
        while q:
            distance += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 2  # Mark as visited
                        q.append((nx, ny))

        return distance
