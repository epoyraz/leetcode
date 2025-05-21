class Solution:
    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        res = []

        def dfs(r, c):
            # Expand as far right and down as possible
            r2, c2 = r, c
            while r2 + 1 < m and land[r2 + 1][c] == 1:
                r2 += 1
            while c2 + 1 < n and land[r][c2 + 1] == 1:
                c2 += 1

            # Mark the entire rectangle as visited
            for i in range(r, r2 + 1):
                for j in range(c, c2 + 1):
                    land[i][j] = 0
            return [r, c, r2, c2]

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    res.append(dfs(i, j))

        return res
