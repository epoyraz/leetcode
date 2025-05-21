class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7
        # dp[i][j]: number of ways to be at cell (i,j) after current number of moves
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0

        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    ways = dp[i][j]
                    if ways:
                        # try all four directions
                        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < m and 0 <= nj < n:
                                new_dp[ni][nj] = (new_dp[ni][nj] + ways) % MOD
                            else:
                                # moving out of bounds: count as a valid path
                                result = (result + ways) % MOD
            dp = new_dp

        return result
