class Solution:
    def prisonAfterNDays(self, cells, n):
        seen = {}
        is_cycle = False

        while n > 0:
            state = tuple(cells)
            if state in seen:
                cycle_len = seen[state] - n
                n %= cycle_len
            else:
                seen[state] = n

            if n == 0:
                break

            n -= 1
            cells = [0] + [int(cells[i - 1] == cells[i + 1]) for i in range(1, 7)] + [0]

        return cells
