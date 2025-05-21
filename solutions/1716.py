class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp_max[i][j], dp_min[i][j]: max/min product to reach (i,j)
        dp_max = [[None]*n for _ in range(m)]
        dp_min = [[None]*n for _ in range(m)]
        
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                candidates = []
                
                # from top
                if i > 0 and dp_max[i-1][j] is not None:
                    candidates.append(dp_max[i-1][j] * val)
                    candidates.append(dp_min[i-1][j] * val)
                
                # from left
                if j > 0 and dp_max[i][j-1] is not None:
                    candidates.append(dp_max[i][j-1] * val)
                    candidates.append(dp_min[i][j-1] * val)
                
                if candidates:
                    dp_max[i][j] = max(candidates)
                    dp_min[i][j] = min(candidates)
        
        res = dp_max[m-1][n-1]
        if res is None or res < 0:
            return -1
        return res % MOD
