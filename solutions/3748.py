class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        # Process each diagonal identified by d = j - i
        for d in range(-(n-1), n):
            # collect the positions along this diagonal
            i_start = max(0, -d)
            i_end   = min(n-1, n-1-d)
            vals = []
            for i in range(i_start, i_end+1):
                j = i + d
                vals.append(grid[i][j])
            # sort according to which triangle we're in
            # bottom-left (d <= 0): non-increasing
            # top-right   (d >  0): non-decreasing
            if d <= 0:
                vals.sort(reverse=True)
            else:
                vals.sort()
            # write back in the same traversal order
            idx = 0
            for i in range(i_start, i_end+1):
                j = i + d
                grid[i][j] = vals[idx]
                idx += 1

        return grid
