class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        
        # 1) Total sum
        total = 0
        for row in grid:
            total += sum(row)
        # If odd, can't split equally
        if total & 1:
            return False
        half = total // 2
        
        # 2) Try horizontal cuts
        racc = 0
        for i in range(m):
            racc += sum(grid[i])
            # cut after row i â upper block is rows [0..i], lower [i+1..m-1]
            if racc == half and i < m - 1:
                return True
        
        # 3) Try vertical cuts
        # build column sums
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]
        
        cacc = 0
        for j in range(n):
            cacc += col_sums[j]
            # cut after col j â left block cols [0..j], right [j+1..n-1]
            if cacc == half and j < n - 1:
                return True
        
        return False
