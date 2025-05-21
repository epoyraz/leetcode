class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # build 2D prefix sums
        # PS[i][j] = sum over r<=i, c<=j of grid[r][c]
        PS = [[0]*n for _ in range(m)]
        count = 0
        
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                PS[i][j] = row_sum
                if i > 0:
                    PS[i][j] += PS[i-1][j]
                
                # if the submatrix (0,0)-(i,j) has sum <= k, count it
                if PS[i][j] <= k:
                    count += 1
        
        return count
