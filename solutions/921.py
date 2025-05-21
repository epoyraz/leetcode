class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        result = []
        steps = 1
        x, y = rStart, cStart
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # E, S, W, N
        dir_idx = 0

        while len(result) < rows * cols:
            for _ in range(2):
                dx, dy = dirs[dir_idx]
                for _ in range(steps):
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                    x += dx
                    y += dy
                dir_idx = (dir_idx + 1) % 4
            steps += 1

        return result
