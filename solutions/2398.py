class Solution:
    def checkXMatrix(self, grid):
        n = len(grid)
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                # On a diagonal?
                if i == j or i + j == n - 1:
                    if val == 0:
                        return False
                else:
                    if val != 0:
                        return False
        return True
