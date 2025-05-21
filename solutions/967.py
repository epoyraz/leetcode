class Solution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        
        for row in range(1, n):
            for col in range(n):
                min_above = matrix[row - 1][col]
                if col > 0:
                    min_above = min(min_above, matrix[row - 1][col - 1])
                if col < n - 1:
                    min_above = min(min_above, matrix[row - 1][col + 1])
                matrix[row][col] += min_above

        return min(matrix[-1])
