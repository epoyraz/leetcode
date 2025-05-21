class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])

        # dp[i][j] = [horizontal 1s ending at (i,j), vertical 1s ending at (i,j)]
        hor = [[0]*n for _ in range(m)]
        ver = [[0]*n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i][j] = hor[i][j-1] + 1 if j > 0 else 1
                    ver[i][j] = ver[i-1][j] + 1 if i > 0 else 1

                    # Try to form the biggest square with (i,j) as bottom-right
                    small = min(hor[i][j], ver[i][j])
                    while small > 0:
                        if hor[i - small + 1][j] >= small and ver[i][j - small + 1] >= small:
                            max_side = max(max_side, small)
                            break
                        small -= 1

        return max_side * max_side
