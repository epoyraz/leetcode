class Solution(object):
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])

        # Ensure the first column is all 1s by flipping rows if needed
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        # For each column, maximize number of 1s
        res = 0
        for j in range(n):
            count = sum(grid[i][j] for i in range(m))
            count = max(count, m - count)
            res += count * (1 << (n - j - 1))
        
        return res
