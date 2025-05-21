class Solution:
    def tictactoe(self, moves):
        rows = [0] * 3
        cols = [0] * 3
        diag = anti_diag = 0

        for i, (r, c) in enumerate(moves):
            player = 1 if i % 2 == 0 else -1  # A = 1, B = -1
            rows[r] += player
            cols[c] += player
            if r == c:
                diag += player
            if r + c == 2:
                anti_diag += player

            if 3 in (rows[r], cols[c], diag, anti_diag):
                return "A"
            if -3 in (rows[r], cols[c], diag, anti_diag):
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"
