class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                            dp[i-1][j],      # top
                            dp[i][j-1],      # left
                            dp[i-1][j-1]     # top-left
                        ) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
