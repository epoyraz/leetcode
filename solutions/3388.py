class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # Precompute row and column totals of 1s
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # pick one other 1 in this row and one other in this column
                    total += (row_counts[i] - 1) * (col_counts[j] - 1)
        return total
