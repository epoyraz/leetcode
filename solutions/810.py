class Solution(object):
    def validTicTacToe(self, board):
        def win(p):
            for i in range(3):
                if all(board[i][j] == p for j in range(3)) or all(board[j][i] == p for j in range(3)):
                    return True
            if all(board[i][i] == p for i in range(3)) or all(board[i][2-i] == p for i in range(3)):
                return True
            return False
        
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        
        if o_count > x_count or x_count > o_count + 1:
            return False
        if win('X') and x_count != o_count + 1:
            return False
        if win('O') and x_count != o_count:
            return False
        return True
