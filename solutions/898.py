class Solution(object):
    def transpose(self, matrix):
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
