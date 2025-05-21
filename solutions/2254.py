class Solution:
    def checkValid(self, matrix):
        n = len(matrix)
        required = set(range(1, n + 1))

        for i in range(n):
            if set(matrix[i]) != required:
                return False
            if set(matrix[j][i] for j in range(n)) != required:
                return False

        return True
