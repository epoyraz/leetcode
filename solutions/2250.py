from collections import deque

class Solution:
    def highestRankedKItems(self, grid, pricing, start, k):
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start
        visited = [[False]*n for _ in range(m)]
        queue = deque()
        queue.append((sr, sc, 0))  # (row, col, distance)
        visited[sr][sc] = True
        result = []

        while queue:
            r, c, dist = queue.popleft()
            val = grid[r][c]
            if low <= val <= high:
                result.append((dist, val, r, c))
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

        result.sort()
        return [[r, c] for _, _, r, c in result[:k]]
