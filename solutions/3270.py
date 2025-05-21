class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        # Check if rook can capture queen directly (same row)
        if a == e:
            col_min, col_max = sorted([b, f])
            if not (col_min < d < col_max and c == a):  # bishop not blocking
                return 1
        # Check if rook can capture queen directly (same column)
        if b == f:
            row_min, row_max = sorted([a, e])
            if not (row_min < c < row_max and d == b):  # bishop not blocking
                return 1

        # Check if bishop can capture queen directly (diagonal)
        if abs(c - e) == abs(d - f):
            dx = 1 if e > c else -1
            dy = 1 if f > d else -1
            x, y = c + dx, d + dy
            blocked = False
            while (x, y) != (e, f):
                if (x, y) == (a, b):  # rook blocks bishop
                    blocked = True
                    break
                x += dx
                y += dy
            if not blocked:
                return 1

        return 2
