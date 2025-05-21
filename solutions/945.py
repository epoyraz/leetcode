class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        
        def label_to_pos(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            if quot % 2 == 0:
                col = rem
            else:
                col = n - 1 - rem
            return row, col
        
        from collections import deque
        visited = set([1])
        q = deque([(1, 0)])  # (square, moves)
        
        while q:
            s, moves = q.popleft()
            if s == n * n:
                return moves
            for s2 in range(s + 1, min(s + 6, n * n) + 1):
                r, c = label_to_pos(s2)
                dest = board[r][c] if board[r][c] != -1 else s2
                if dest not in visited:
                    visited.add(dest)
                    q.append((dest, moves + 1))
        return -1
