class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Base case: 1x1 grid
        if n == 0:
            return [[0]]
        
        # Recursive build of smaller (2^(n-1) x 2^(n-1)) special grid
        small = self.specialGrid(n - 1)
        m = 1 << (n - 1)          # size of small grid
        size = m << 1             # size of new grid = 2*m
        chunk = m * m             # number of entries in each quadrant
        
        # Initialize the 2^n x 2^n result grid
        grid = [[0] * size for _ in range(size)]
        
        # Quadrant offsets: TR=0, BR=1, BL=2, TL=3 (in increasing value order)
        # Fill Top-Right (rows 0..m-1, cols m..2m-1)
        for i in range(m):
            for j in range(m):
                grid[i][j + m] = small[i][j] + 0 * chunk
        
        # Fill Bottom-Right (rows m..2m-1, cols m..2m-1)
        for i in range(m):
            for j in range(m):
                grid[i + m][j + m] = small[i][j] + 1 * chunk
        
        # Fill Bottom-Left (rows m..2m-1, cols 0..m-1)
        for i in range(m):
            for j in range(m):
                grid[i + m][j] = small[i][j] + 2 * chunk
        
        # Fill Top-Left (rows 0..m-1, cols 0..m-1)
        for i in range(m):
            for j in range(m):
                grid[i][j] = small[i][j] + 3 * chunk
        
        return grid
