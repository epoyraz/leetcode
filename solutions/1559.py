class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        # dp[c1][c2] = max cherries collected when robot1 is at column c1
        # and robot2 is at column c2 on the current row
        # initialize for row 0
        dp = [[-float('inf')] * cols for _ in range(cols)]
        dp[0][cols-1] = grid[0][0] + grid[0][cols-1]
        
        for r in range(1, rows):
            new_dp = [[-float('inf')] * cols for _ in range(cols)]
            for c1 in range(cols):
                for c2 in range(cols):
                    if dp[c1][c2] < 0:
                        continue
                    # try all moves for both robots
                    for nc1 in (c1-1, c1, c1+1):
                        for nc2 in (c2-1, c2, c2+1):
                            if 0 <= nc1 < cols and 0 <= nc2 < cols:
                                val = dp[c1][c2] + grid[r][nc1]
                                if nc1 != nc2:
                                    val += grid[r][nc2]
                                if val > new_dp[nc1][nc2]:
                                    new_dp[nc1][nc2] = val
            dp = new_dp
        
        # answer is the max over final positions
        ans = 0
        for c1 in range(cols):
            for c2 in range(cols):
                if dp[c1][c2] > ans:
                    ans = dp[c1][c2]
        return ans
