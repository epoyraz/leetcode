class Solution(object):
    def numMagicSquaresInside(self, grid):
        def is_magic(r, c):
            s = set()
            for i in range(3):
                for j in range(3):
                    if not (1 <= grid[r+i][c+j] <= 9):
                        return False
                    s.add(grid[r+i][c+j])
            if len(s) != 9:
                return False
            rows = [sum(grid[r+i][c:c+3]) for i in range(3)]
            cols = [sum(grid[r+i][c+j] for i in range(3)) for j in range(3)]
            diag1 = sum(grid[r+i][c+i] for i in range(3))
            diag2 = sum(grid[r+i][c+2-i] for i in range(3))
            return len(set(rows + cols + [diag1, diag2])) == 1
        
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m-2):
            for j in range(n-2):
                if grid[i+1][j+1] == 5 and is_magic(i, j):
                    count += 1
        return count
