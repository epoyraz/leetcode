class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initialize boundaries to extreme values
        min_row = float('inf')
        max_row = -float('inf')
        min_col = float('inf')
        max_col = -float('inf')
        
        rows = len(grid)
        cols = len(grid[0])
        
        # scan the grid to update boundaries
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r < min_row:
                        min_row = r
                    if r > max_row:
                        max_row = r
                    if c < min_col:
                        min_col = c
                    if c > max_col:
                        max_col = c
        
        # compute height and width of the enclosing rectangle
        height = max_row - min_row + 1
        width  = max_col - min_col + 1
        
        return height * width
