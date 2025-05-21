from collections import deque

class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        queue = deque()

        # Initialize queue with all 0s and set 1s to -1 as unvisited
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1:
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni, nj))

        return mat
