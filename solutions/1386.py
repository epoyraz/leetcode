class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        # Flatten the grid
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        # Shift
        flat = flat[-k:] + flat[:-k]
        # Reshape
        return [flat[i * n:(i + 1) * n] for i in range(m)]
