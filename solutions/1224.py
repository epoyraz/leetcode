class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        dp = grid[0][:]

        for i in range(1, n):
            new_dp = [0] * n
            # Find the min and second min from the previous row
            min1, min2 = float('inf'), float('inf')
            idx1 = -1

            for j in range(n):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                    idx1 = j
                elif dp[j] < min2:
                    min2 = dp[j]

            for j in range(n):
                if j == idx1:
                    new_dp[j] = grid[i][j] + min2
                else:
                    new_dp[j] = grid[i][j] + min1

            dp = new_dp

        return min(dp)
