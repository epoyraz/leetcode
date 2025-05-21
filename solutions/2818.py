class Solution:
    def maxIncreasingCells(self, mat):
        m, n = len(mat), len(mat[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((mat[i][j], i, j))
        
        cells.sort()  # Process in increasing order of value

        row_best = [0] * m
        col_best = [0] * n
        ans = 0

        i = 0
        while i < len(cells):
            j = i
            updates = []
            # Process all cells with the same value together
            while j < len(cells) and cells[j][0] == cells[i][0]:
                _, r, c = cells[j]
                curr_len = 1 + max(row_best[r], col_best[c])
                updates.append((r, c, curr_len))
                j += 1
            # Commit updates after batch to avoid intra-batch interference
            for r, c, length in updates:
                row_best[r] = max(row_best[r], length)
                col_best[c] = max(col_best[c], length)
                ans = max(ans, length)
            i = j

        return ans
