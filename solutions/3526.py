class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Cost to fix rows
        cost_rows = 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - 1 - j]:
                    cost_rows += 1
        
        # Cost to fix columns
        cost_cols = 0
        for j in range(n):
            for i in range(m // 2):
                if grid[i][j] != grid[m - 1 - i][j]:
                    cost_cols += 1
        
        return min(cost_rows, cost_cols)
