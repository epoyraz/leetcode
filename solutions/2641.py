class Solution(object):
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(x, y, visited):
            if x >= m or y >= n or grid[x][y] == 0 or visited[x][y]:
                return False
            if x == m - 1 and y == n - 1:
                return True
            visited[x][y] = True
            return dfs(x + 1, y, visited) or dfs(x, y + 1, visited)

        # First DFS: mark one valid path from (0,0) to (m-1,n-1)
        visited1 = [[False] * n for _ in range(m)]
        if not dfs(0, 0, visited1):
            return True  # Already disconnected

        # Flip all visited path to 0 (simulate cut)
        for i in range(m):
            for j in range(n):
                if visited1[i][j] and (i != 0 or j != 0) and (i != m - 1 or j != n - 1):
                    grid[i][j] = 0

        # Second DFS: check if any other path exists
        visited2 = [[False] * n for _ in range(m)]
        return not dfs(0, 0, visited2)
