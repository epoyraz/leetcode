class Solution(object):
    def minFlips(self, grid):
        m, n = len(grid), len(grid[0])

        # Collect each 4-cell âorbitâ under row+column reversal
        orbits = []
        for i in range((m + 1)//2):
            for j in range((n + 1)//2):
                cells = {
                    (i, j),
                    (i, n-1-j),
                    (m-1-i, j),
                    (m-1-i, n-1-j)
                }
                ones = sum(grid[x][y] for x, y in cells)
                s = len(cells)
                c0 = ones        # flips to make all 0
                c1 = s - ones    # flips to make all 1
                orbits.append((s, c0, c1))

        INF = float('inf')
        # dp[r] = min flips so far to get total-ones â¡ r (mod 4)
        dp = [0, INF, INF, INF]

        for s, c0, c1 in orbits:
            s_mod = s % 4
            new = [INF]*4
            for r in range(4):
                # option A: set orbit to 0 â ones unchanged
                new[r] = min(new[r], dp[r] + c0)
                # option B: set orbit to 1 â ones += s
                new[(r + s_mod) % 4] = min(new[(r + s_mod) % 4],
                                           dp[r] + c1)
            dp = new

        return dp[0]
