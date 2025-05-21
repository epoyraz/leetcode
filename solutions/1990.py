class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
                # maximum possible "radius" k for a rhombus centered at (i,j)
                k_max = min(i, m - 1 - i, j, n - 1 - j)
                
                # k = 0 is just the single cell
                total = grid[i][j]
                sums.add(total)
                
                # try larger rhombi
                for k in range(1, k_max + 1):
                    border_sum = 0
                    # edge 1: top -> right
                    for t in range(0, k + 1):
                        r, c = i - k + t, j + t
                        border_sum += grid[r][c]
                    # edge 2: right -> bottom
                    for t in range(1, k + 1):
                        r, c = i + t, j + k - t
                        border_sum += grid[r][c]
                    # edge 3: bottom -> left
                    for t in range(1, k + 1):
                        r, c = i + k - t, j - t
                        border_sum += grid[r][c]
                    # edge 4: left -> top
                    for t in range(1, k):
                        r, c = i - t, j - k + t
                        border_sum += grid[r][c]
                    
                    sums.add(border_sum)
        
        # take the top three distinct sums
        return sorted(sums, reverse=True)[:3]
