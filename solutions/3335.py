class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        mid = n // 2
        
        # 1) Collect all coordinates in the "Y" shape
        Y = set()
        # two diagonals from (0,0) and (0,n-1) down to center
        for i in range(mid+1):
            Y.add((i, i))
            Y.add((i, n-1 - i))
        # vertical line from center down to bottom
        for r in range(mid, n):
            Y.add((r, mid))
        
        # 2) Try all (v1, v2) with v1 != v2
        best = float('inf')
        for v1 in (0, 1, 2):
            for v2 in (0, 1, 2):
                if v1 == v2:
                    continue
                ops = 0
                # count mismatches in Y where we want color v1
                for (r, c) in Y:
                    if grid[r][c] != v1:
                        ops += 1
                # count mismatches outside Y where we want v2
                for r in range(n):
                    for c in range(n):
                        if (r, c) not in Y and grid[r][c] != v2:
                            ops += 1
                best = min(best, ops)
        
        return best
