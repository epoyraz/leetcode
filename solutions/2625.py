class Solution:
    def rangeAddQueries(self, n, queries):
        # Initialize difference matrix with 0s
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Step 1: Apply difference array updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            if c2 + 1 < n:
                diff[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                diff[r2 + 1][c2 + 1] += 1

        # Step 2: Convert to prefix sums across rows
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        # Step 3: Convert to prefix sums down columns
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Step 4: Trim to n x n result
        return [diff[i][:n] for i in range(n)]
