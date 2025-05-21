class Solution:
    def maxSum(self, grid):
        m, n = len(grid), len(grid[0])
        max_sum = 0
        for i in range(m - 2):
            for j in range(n - 2):
                # Sum the hourglass with top-left corner at (i,j)
                s = (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                    grid[i+1][j+1] +
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                )
                if s > max_sum:
                    max_sum = s
        return max_sum
