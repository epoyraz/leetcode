class Solution:
    def tilingRectangle(self, n, m):
        if n > m:
            n, m = m, n
        self.res = n * m

        def dfs(grid, count):
            if count >= self.res:
                return
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0:
                        x, y = i, j
                        break
                else:
                    continue
                break
            else:
                self.res = min(self.res, count)
                return

            max_len = min(n - x, m - y)
            for size in range(max_len, 0, -1):
                if all(grid[x + dx][y + dy] == 0 for dx in range(size) for dy in range(size)):
                    for dx in range(size):
                        for dy in range(size):
                            grid[x + dx][y + dy] = 1
                    dfs(grid, count + 1)
                    for dx in range(size):
                        for dy in range(size):
                            grid[x + dx][y + dy] = 0

        dfs([[0] * m for _ in range(n)], 0)
        return self.res
