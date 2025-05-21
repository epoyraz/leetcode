class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Precompute prefix sums for rows and columns
        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]

        def is_magic(r, c, size):
            diag1 = diag2 = 0
            for i in range(size):
                diag1 += grid[r + i][c + i]
                diag2 += grid[r + i][c + size - 1 - i]
            if diag1 != diag2:
                return False
            target = diag1
            for i in range(size):
                rs = row_sum[r + i][c + size] - row_sum[r + i][c]
                cs = col_sum[r + size][c + i] - col_sum[r][c + i]
                if rs != target or cs != target:
                    return False
            return True

        max_k = min(m, n)
        for k in range(max_k, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k
        return 1
