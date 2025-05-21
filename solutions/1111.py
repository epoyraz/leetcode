class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        # dp[i][j] = min score to triangulate polygon from i to j
        dp = [[0]*n for _ in range(n)]
        
        # length = j - i + 1, start from length 3 (one triangle)
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                # pick k between i and j to form triangle (i,k,j)
                for k in range(i+1, j):
                    cost = dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        
        return dp[0][n-1]
