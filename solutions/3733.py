class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        # Directions: 0 = NE, 1 = SE, 2 = SW, 3 = NW
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        # dpStart[i][j][d]: max length starting at (i,j) with a '1', then 2,0,2...
        # dpOdd[i][j][d]:   max length starting at (i,j) on an odd-indexed step (needs '2'), then 0,2...
        # dpEven[i][j][d]:  max length starting at (i,j) on an even-indexed step>=2 (needs '0'), then 2,0...
        dpStart = [[[0]*4 for _ in range(m)] for __ in range(n)]
        dpOdd   = [[[0]*4 for _ in range(m)] for __ in range(n)]
        dpEven  = [[[0]*4 for _ in range(m)] for __ in range(n)]

        def fill_dir(d):
            dx, dy = dirs[d]
            # scan order so that (i+dx, j+dy) is already computed
            i_range = range(n) if dx < 0 else range(n-1, -1, -1)
            j_range = range(m) if dy < 0 else range(m-1, -1, -1)
            for i in i_range:
                for j in j_range:
                    ni, nj = i + dx, j + dy
                    # odd step: cell must be '2'
                    if grid[i][j] == 2:
                        dpOdd[i][j][d] = 1
                        if 0 <= ni < n and 0 <= nj < m:
                            dpOdd[i][j][d] += dpEven[ni][nj][d]
                    # even step: cell must be '0'
                    if grid[i][j] == 0:
                        dpEven[i][j][d] = 1
                        if 0 <= ni < n and 0 <= nj < m:
                            dpEven[i][j][d] += dpOdd[ni][nj][d]
                    # start step: cell must be '1'
                    if grid[i][j] == 1:
                        dpStart[i][j][d] = 1
                        if 0 <= ni < n and 0 <= nj < m:
                            dpStart[i][j][d] += dpOdd[ni][nj][d]

        # fill DP for each diagonal direction
        for d in range(4):
            fill_dir(d)

        best = 0
        # try every start cell and initial direction
        for i in range(n):
            for j in range(m):
                for d in range(4):
                    L = dpStart[i][j][d]
                    best = max(best, L)        # straight
                    if L == 0:
                        continue
                    dx, dy = dirs[d]
                    d2 = (d + 1) & 3           # clockwise turn
                    dx2, dy2 = dirs[d2]
                    ci, cj = i, j
                    # consider turning after each prefix of length k+1
                    for k in range(1, L):
                        ci += dx
                        cj += dy
                        ni, nj = ci + dx2, cj + dy2
                        if not (0 <= ni < n and 0 <= nj < m):
                            break
                        # next step index is k+1 â parity = (k+1)&1
                        if (k+1) & 1:
                            l2 = dpOdd[ni][nj][d2]
                        else:
                            l2 = dpEven[ni][nj][d2]
                        best = max(best, (k+1) + l2)

        return best
