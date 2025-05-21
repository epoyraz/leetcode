class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        # Map each value to its (row, col) in mat
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)
                
        # Counters for painted cells in each row/column
        row_cnt = [0] * m
        col_cnt = [0] * n
        
        # Paint in the order given by arr
        for idx, v in enumerate(arr):
            r, c = pos[v]
            row_cnt[r] += 1
            col_cnt[c] += 1
            # Check if this row or column is now fully painted
            if row_cnt[r] == n or col_cnt[c] == m:
                return idx
        
        # Per problem statement this should never happen, but just in case:
        return -1
