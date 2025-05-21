class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        dp = [[[float('-inf')] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]
        
        for k in range(1, 2 * n - 1):
            temp = [[[float('-inf')] * n for _ in range(n)] for _ in range(n)]
            for x1 in range(max(0, k - (n - 1)), min(n, k + 1)):
                y1 = k - x1
                if y1 >= n or grid[x1][y1] == -1:
                    continue
                for x2 in range(max(0, k - (n - 1)), min(n, k + 1)):
                    y2 = k - x2
                    if y2 >= n or grid[x2][y2] == -1:
                        continue
                    best = float('-inf')
                    for preX1, preX2 in [(x1 - 1, x2 - 1), (x1 - 1, x2), (x1, x2 - 1), (x1, x2)]:
                        if 0 <= preX1 < n and 0 <= preX2 < n:
                            best = max(best, dp[preX1][preX2][k-1-preX1-preX2])
                    if best != float('-inf'):
                        temp[x1][x2][k-x1-x2] = best + grid[x1][y1] + (grid[x2][y2] if (x1, y1) != (x2, y2) else 0)
            dp = temp
        return max(0, dp[n-1][n-1][0])
