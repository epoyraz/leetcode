class Solution(object):
    def maxScore(self, grid):
        rows = len(grid)
        # Precompute for each row the set of values in that row
        row_vals = [set(r) for r in grid]
        # List of distinct values across the grid
        distinct = sorted({v for row in grid for v in row})
        
        # DP[mask] = max score using values processed so far,
        # assigning to rows indicated by bits in mask
        # mask bit i = 1 means row i has been assigned a value
        N = 1 << rows
        DP = [-10**18] * N
        DP[0] = 0
        
        for v in distinct:
            DP2 = DP[:]  # copy previous
            # Try assigning this value v to any one unassigned row
            for mask in range(N):
                cur = DP[mask]
                if cur < 0:
                    continue
                # rows not yet assigned
                avail = (~mask) & (N - 1)
                # iterate through set bits
                while avail:
                    i = (avail & -avail).bit_length() - 1
                    if v in row_vals[i]:
                        nm = mask | (1 << i)
                        DP2[nm] = max(DP2[nm], cur + v)
                    avail &= avail - 1
            DP = DP2
        
        # The answer is the maximum over all masks
        return max(DP)
