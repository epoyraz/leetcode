class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        dp = [[0] * (i + 1) for i in range(query_row + 2)]
        dp[0][0] = poured
        
        for r in range(query_row + 1):
            for c in range(len(dp[r])):
                if dp[r][c] > 1:
                    excess = dp[r][c] - 1
                    dp[r+1][c] += excess / 2.0
                    dp[r+1][c+1] += excess / 2.0
                    dp[r][c] = 1
        
        return dp[query_row][query_glass]
