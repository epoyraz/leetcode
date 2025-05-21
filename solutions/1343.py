class Solution:
    def dieSimulator(self, n, rollMax):
        MOD = 10**9 + 7
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n+1)]
        
        for i in range(6):
            dp[1][i][1] = 1
        
        for i in range(2, n+1):
            for j in range(6):  # current face
                for k in range(6):  # previous face
                    for c in range(1, rollMax[k]+1):
                        if j == k and c + 1 <= rollMax[j]:
                            dp[i][j][c+1] = (dp[i][j][c+1] + dp[i-1][j][c]) % MOD
                        elif j != k:
                            dp[i][j][1] = (dp[i][j][1] + dp[i-1][k][c]) % MOD
        
        res = 0
        for j in range(6):
            for c in range(1, rollMax[j]+1):
                res = (res + dp[n][j][c]) % MOD
        return res
