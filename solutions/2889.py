from collections import defaultdict

class Solution:
    def countBlackBlocks(self, m, n, coordinates):
        block_count = defaultdict(int)
        black = set((x, y) for x, y in coordinates)

        for x, y in black:
            for dx in (0, -1):
                for dy in (0, -1):
                    i, j = x + dx, y + dy
                    if 0 <= i < m - 1 and 0 <= j < n - 1:
                        block_count[(i, j)] += 1

        result = [0] * 5
        for cnt in block_count.values():
            result[cnt] += 1

        total_blocks = (m - 1) * (n - 1)
        result[0] = total_blocks - sum(result[1:])

        return result
