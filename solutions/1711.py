class Solution:
    def restoreMatrix(self, rowSum, colSum):
        m, n = len(rowSum), len(colSum)
        # initialize mÃn zero matrix
        ans = [[0]*n for _ in range(m)]
        i = j = 0

        # march through rows and columns
        while i < m and j < n:
            # take the max we can here without overshooting
            take = min(rowSum[i], colSum[j])
            ans[i][j] = take
            rowSum[i]  -= take
            colSum[j]  -= take

            # if we've satisfied row i, move to next row
            if rowSum[i] == 0:
                i += 1
            # if we've satisfied column j, move to next column
            if colSum[j] == 0:
                j += 1

        return ans
