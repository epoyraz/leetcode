class Solution:
    def minPathCost(self, grid, moveCost):
        m, n = len(grid), len(grid[0])
        # dp[j] = min cost to reach cell in current row at column j
        dp = [grid[0][j] for j in range(n)]
        
        # Process each subsequent row
        for i in range(1, m):
            new_dp = [float('inf')] * n
            for prev_col in range(n):
                prev_val = grid[i-1][prev_col]
                base = dp[prev_col] + moveCost[prev_val][0]  # placeholder
                for col in range(n):
                    cost = dp[prev_col] + moveCost[prev_val][col] + grid[i][col]
                    if cost < new_dp[col]:
                        new_dp[col] = cost
            dp = new_dp
        
        # The answer is the min cost among the last row
        return min(dp)
