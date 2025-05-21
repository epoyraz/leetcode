class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        grid = [[n] * n for _ in range(n)]
        banned = set(tuple(mine) for mine in mines)
        
        for i in range(n):
            count = 0
            for j in range(n):
                count = 0 if (i, j) in banned else count + 1
                grid[i][j] = min(grid[i][j], count)
            count = 0
            for j in range(n-1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                grid[i][j] = min(grid[i][j], count)
        
        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if (i, j) in banned else count + 1
                grid[i][j] = min(grid[i][j], count)
            count = 0
            for i in range(n-1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                grid[i][j] = min(grid[i][j], count)
        
        return max(max(row) for row in grid)
