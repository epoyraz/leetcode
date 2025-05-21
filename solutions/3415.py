class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                # Check equality with the cell below
                if i + 1 < m and grid[i][j] != grid[i + 1][j]:
                    return False
                # Check inequality with the cell to the right
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    return False
        
        return True
