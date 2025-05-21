class Solution:
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
                    break

        result = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx + dx < 8 and 0 <= ny + dy < 8:
                nx += dx
                ny += dy
                if board[nx][ny] == 'B':
                    break
                if board[nx][ny] == 'p':
                    result += 1
                    break

        return result
