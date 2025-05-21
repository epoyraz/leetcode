class Solution:
    def maxTrailingZeros(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Step 1: factor each cell into counts of 2s and 5s
        f2 = [[0]*n for _ in range(m)]
        f5 = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                c2 = c5 = 0
                while x % 2 == 0:
                    x //= 2; c2 += 1
                while x % 5 == 0:
                    x //= 5; c5 += 1
                f2[i][j], f5[i][j] = c2, c5

        # Step 2: build rowâprefixes and rowâsuffixes of f2/f5
        row2 = [[0]*n for _ in range(m)]
        row5 = [[0]*n for _ in range(m)]
        row2r = [[0]*n for _ in range(m)]
        row5r = [[0]*n for _ in range(m)]
        for i in range(m):
            a2 = a5 = 0
            for j in range(n):
                a2 += f2[i][j]
                a5 += f5[i][j]
                row2[i][j], row5[i][j] = a2, a5
            a2 = a5 = 0
            for j in range(n-1, -1, -1):
                a2 += f2[i][j]
                a5 += f5[i][j]
                row2r[i][j], row5r[i][j] = a2, a5

        # Step 3: build columnâprefixes and columnâsuffixes of f2/f5
        col2 = [[0]*n for _ in range(m)]
        col5 = [[0]*n for _ in range(m)]
        col2r = [[0]*n for _ in range(m)]
        col5r = [[0]*n for _ in range(m)]
        for j in range(n):
            a2 = a5 = 0
            for i in range(m):
                a2 += f2[i][j]
                a5 += f5[i][j]
                col2[i][j], col5[i][j] = a2, a5
            a2 = a5 = 0
            for i in range(m-1, -1, -1):
                a2 += f2[i][j]
                a5 += f5[i][j]
                col2r[i][j], col5r[i][j] = a2, a5

        # Step 4: try each cell as the âcornerâ of the L
        best = 0
        for i in range(m):
            for j in range(n):
                # For convenience
                c2, c5 = f2[i][j], f5[i][j]

                # 4 choices: up+left, up+right, down+left, down+right
                # each = (vertical leg) + (horizontal leg) â (cell counted twice)
                # and trailing zeros = min(total2, total5)
                
                # up + left
                t2 = col2[i][j] + row2[i][j] - c2
                t5 = col5[i][j] + row5[i][j] - c5
                best = max(best, min(t2, t5))
                
                # up + right
                t2 = col2[i][j] + row2r[i][j] - c2
                t5 = col5[i][j] + row5r[i][j] - c5
                best = max(best, min(t2, t5))
                
                # down + left
                t2 = col2r[i][j] + row2[i][j] - c2
                t5 = col5r[i][j] + row5[i][j] - c5
                best = max(best, min(t2, t5))
                
                # down + right
                t2 = col2r[i][j] + row2r[i][j] - c2
                t5 = col5r[i][j] + row5r[i][j] - c5
                best = max(best, min(t2, t5))

        return best
