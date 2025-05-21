class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None. Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def countLiveNeighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          ( 0, -1),          ( 0, 1),
                          ( 1, -1), ( 1, 0), ( 1, 1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in [1, 2]:
                    count += 1
            return count

        # First pass: encode changes
        for i in range(m):
            for j in range(n):
                live_neighbors = countLiveNeighbors(i, j)

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Live â Dead
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 3  # Dead â Live

        # Second pass: finalize new state
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
