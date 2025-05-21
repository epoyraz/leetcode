class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        # compute max of each column ignoring -1
        col_max = []
        for j in range(n):
            mj = matrix[0][j]
            for i in range(1, m):
                v = matrix[i][j]
                if v > mj:
                    mj = v
            # if mj is -1 (all -1), but problem guarantees at least one non-negative per column
            col_max.append(mj)
        # build answer
        answer = [row[:] for row in matrix]
        for i in range(m):
            for j in range(n):
                if answer[i][j] == -1:
                    answer[i][j] = col_max[j]
        return answer
