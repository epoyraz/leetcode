class Solution:
    def oddCells(self, m, n, indices):
        row = [0] * m
        col = [0] * n

        for r, c in indices:
            row[r] += 1
            col[c] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2 == 1:
                    count += 1

        return count
