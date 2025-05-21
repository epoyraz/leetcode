class Solution:
    def isRobotBounded(self, instructions):
        x = y = 0
        dx, dy = 0, 1  # facing north
        for ch in instructions:
            if ch == 'G':
                x += dx
                y += dy
            elif ch == 'L':
                dx, dy = -dy, dx
            else:  # 'R'
                dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)
