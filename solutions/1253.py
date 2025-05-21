from collections import defaultdict

class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # Collect values of each diagonal keyed by (i - j)
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
        
        # Sort each diagonal's list in reverse to pop smallest efficiently
        for key in diagonals:
            diagonals[key].sort(reverse=True)
        
        # Write back the sorted values
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        
        return mat
