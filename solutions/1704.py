class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0]) if m else 0
        
        # count 1s in each row and column
        row_counts = [sum(row) for row in mat]
        col_counts = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        # a position is special if it's 1 and its row and column sums are both 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_counts[i] == 1 and col_counts[j] == 1:
                    ans += 1
        return ans
