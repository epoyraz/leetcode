class Solution:
    def differenceOfDistinctValues(self, grid):
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                # Scan upper-left diagonal
                i, j = r - 1, c - 1
                left_set = set()
                while i >= 0 and j >= 0:
                    left_set.add(grid[i][j])
                    i -= 1
                    j -= 1

                # Scan bottom-right diagonal
                i, j = r + 1, c + 1
                right_set = set()
                while i < m and j < n:
                    right_set.add(grid[i][j])
                    i += 1
                    j += 1

                ans[r][c] = abs(len(left_set) - len(right_set))

        return ans
