class Solution(object):
    def ways(self, pizza, k):
        mod = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        # suffix sum of apples
        apples = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                apples[i][j] = (1 if pizza[i][j]=='A' else 0) + apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
        # dp[c][i][j]: ways to cut starting at (i,j) into c pieces
        dp = [[[0]*cols for _ in range(rows)] for _ in range(k+1)]
        # base: one piece, must have at least one apple
        for i in range(rows):
            for j in range(cols):
                if apples[i][j] > 0:
                    dp[1][i][j] = 1
        # build up
        for c in range(2, k+1):
            for i in range(rows):
                for j in range(cols):
                    # horizontal cuts
                    for ni in range(i+1, rows):
                        if apples[i][j] - apples[ni][j] > 0:
                            dp[c][i][j] = (dp[c][i][j] + dp[c-1][ni][j]) % mod
                    # vertical cuts
                    for nj in range(j+1, cols):
                        if apples[i][j] - apples[i][nj] > 0:
                            dp[c][i][j] = (dp[c][i][j] + dp[c-1][i][nj]) % mod
        return dp[k][0][0]
