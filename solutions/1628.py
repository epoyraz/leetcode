class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        res = 0
        heights = [0] * n

        for i in range(m):
            for j in range(n):
                # Build histogram for row i
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Count rectangles using stack
            stack = []
            count = [0] * n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                if stack:
                    prev = stack[-1]
                    count[j] = count[prev] + heights[j] * (j - prev)
                else:
                    count[j] = heights[j] * (j + 1)
                res += count[j]
                stack.append(j)

        return res
