class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        opp = 'W' if color == 'B' else 'B'
        n = 8
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0),  (1, 1)]
        
        for dx, dy in dirs:
            x, y = rMove + dx, cMove + dy
            if not (0 <= x < n and 0 <= y < n and board[x][y] == opp):
                continue
            step = 2
            while True:
                nx = rMove + dx * step
                ny = cMove + dy * step
                if not (0 <= nx < n and 0 <= ny < n):
                    break
                cell = board[nx][ny]
                if cell == '.':
                    break
                if cell == color:
                    return True
                step += 1
        return False
