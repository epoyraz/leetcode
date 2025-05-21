class Solution:
    def countSubIslands(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            res = True
            if grid1[i][j] == 0:
                res = False
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not dfs(i + dx, j + dy):
                    res = False
            return res

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        return count
