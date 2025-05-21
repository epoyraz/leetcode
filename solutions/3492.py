class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        # prev prefix sums for X and Y up through previous row
        prev_px = [0] * (m+1)
        prev_py = [0] * (m+1)
        
        for i in xrange(1, n+1):
            row = grid[i-1]
            cur_px = [0] * (m+1)
            cur_py = [0] * (m+1)
            for j in xrange(1, m+1):
                c = row[j-1]
                isX = 1 if c == 'X' else 0
                isY = 1 if c == 'Y' else 0
                
                # 2D prefix sum relation
                cur_px[j] = (cur_px[j-1]
                             + prev_px[j]
                             - prev_px[j-1]
                             + isX)
                cur_py[j] = (cur_py[j-1]
                             + prev_py[j]
                             - prev_py[j-1]
                             + isY)
                
                # submatrix from (0,0) to (i-1,j-1):
                # needs at least one X and equal X/Y counts
                if cur_px[j] > 0 and cur_px[j] == cur_py[j]:
                    ans += 1
            
            # advance prev to this row
            prev_px = cur_px
            prev_py = cur_py
        
        return ans
