class Solution:
    def queensAttacktheKing(self, queens, king):
        board = [[0]*8 for _ in range(8)]
        for x, y in queens:
            board[x][y] = 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        res = []
        for dx, dy in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == 1:
                    res.append([x, y])
                    break
        return res
