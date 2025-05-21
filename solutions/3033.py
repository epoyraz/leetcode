class Solution(object):
    def minOperations(self, s1, s2, x):
       # Build list of mismatch positions
        d = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        m = len(d)
        if m % 2:
            return -1
        
        # If no mismatches, cost is 0
        if m == 0:
            return 0
        
        # Precompute pairwise costs: cost to flip exactly positions i and j
        # via adjacent flips (distance) or via the x-cost op.
        # cost(i,j) = min(x, |d[j] - d[i]|)
        cost = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i+1, m):
                dist = d[j] - d[i]
                cost[i][j] = cost[j][i] = min(x, dist)
        
        # dp[i][j] = minimum cost to perfectly match (clear) mismatches
        # in the subarray d[i..j], inclusive. Only defined when (j-i+1) is even.
        INF = 10**18
        dp = [[0] * m for _ in range(m)]
        
        # Initialize dp for all even-length segments
        # length = number of elements in segment
        for length in range(2, m+1, 2):
            for i in range(0, m - length + 1):
                j = i + length - 1
                # Option 1: pair ends (i, j) together
                best = dp[i+1][j-1] + cost[i][j]
                # Option 2: split the segment into two even parts at k
                # k runs over odd offsets so that both subsegments are even-length
                for k in range(i+1, j, 2):
                    val = dp[i][k] + dp[k+1][j]
                    if val < best:
                        best = val
                dp[i][j] = best
        
        return dp[0][m-1]
