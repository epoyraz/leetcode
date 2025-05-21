class Solution:
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        m, n = len(grid), len(grid[0])
        
        # Step 1: Prefix sum matrix
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i+1][j+1] = grid[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]

        # Step 2: Mark where stamps can be placed
        can_stamp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                r1, c1 = i, j
                r2, c2 = i + stampHeight, j + stampWidth
                total = pre[r2][c2] - pre[r2][c1] - pre[r1][c2] + pre[r1][c1]
                if total == 0:
                    can_stamp[i][j] += 1
                    can_stamp[i][j + stampWidth] -= 1
                    can_stamp[i + stampHeight][j] -= 1
                    can_stamp[i + stampHeight][j + stampWidth] += 1

        # Step 3: 2D prefix sum of stamp influence
        for i in range(m + 1):
            for j in range(1, n + 1):
                can_stamp[i][j] += can_stamp[i][j - 1]
        for i in range(1, m + 1):
            for j in range(n + 1):
                can_stamp[i][j] += can_stamp[i - 1][j]

        # Step 4: Verify all empty cells are covered
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and can_stamp[i][j] == 0:
                    return False
        return True
