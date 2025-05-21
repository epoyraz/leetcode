class Solution:
    def matrixBlockSum(self, mat, k):
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Compute prefix sum
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
        
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m, i + k + 1), min(n, j + k + 1)
                res[i][j] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
        
        return res
