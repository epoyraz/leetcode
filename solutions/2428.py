class Solution:
    def equalPairs(self, grid):
        from collections import Counter
        
        n = len(grid)
        # Count each row as a tuple
        row_counts = Counter(tuple(row) for row in grid)
        
        ans = 0
        # For each column, form its tuple and add how many matching rows there are
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            ans += row_counts[col]
        
        return ans
