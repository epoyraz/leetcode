class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n-1-i]
        if n % 2 == 1:
            total -= mat[n//2][n//2]
        return total
