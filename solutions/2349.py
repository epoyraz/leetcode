class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        # Quick checks
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        # dp[i][j] = set of possible balances at cell (i,j)
        dp = [ [set() for _ in range(n)] for _ in range(m) ]
        # Start at (0,0) with balance 1
        dp[0][0].add(1)
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                char = grid[i][j]
                balances = set()
                # Gather from top
                if i > 0:
                    balances |= dp[i-1][j]
                # Gather from left
                if j > 0:
                    balances |= dp[i][j-1]
                if not balances:
                    continue
                new_bal = set()
                if char == '(':
                    # increase every balance by 1
                    for b in balances:
                        new_bal.add(b+1)
                else:
                    # char == ')', decrease if possible
                    for b in balances:
                        if b > 0:
                            new_bal.add(b-1)
                dp[i][j] = new_bal
        
        # Check if 0 balance at destination
        return 0 in dp[m-1][n-1]
