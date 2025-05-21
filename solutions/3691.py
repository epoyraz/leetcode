class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        total_ops = 0

        for col in range(n):
            prev = grid[0][col]
            for row in range(1, m):
                if grid[row][col] <= prev:
                    ops = prev + 1 - grid[row][col]
                    total_ops += ops
                    grid[row][col] += ops
                prev = grid[row][col]

        return total_ops
