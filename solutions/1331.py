class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        max_gold = 0

        def dfs(i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
                return 0

            visited[i][j] = True
            gold = grid[i][j]
            max_val = 0
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                max_val = max(max_val, dfs(i+dx, j+dy, visited))
            visited[i][j] = False
            return gold + max_val

        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j, visited))

        return max_gold
