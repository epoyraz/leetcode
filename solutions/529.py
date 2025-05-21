class Solution:
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        
        def count_mines(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    count += 1
            return count

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != 'E':
                return
            mine_count = count_mines(x, y)
            if mine_count > 0:
                board[x][y] = str(mine_count)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    dfs(x + dx, y + dy)

        cx, cy = click
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
        else:
            dfs(cx, cy)

        return board
