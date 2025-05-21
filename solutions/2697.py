from collections import deque
import bisect

class Solution:
    def minimumVisitedCells(self, grid):
        m, n = len(grid), len(grid[0])
        # Available unvisited columns per row and rows per column
        row_avail = [list(range(n)) for _ in range(m)]
        col_avail = [list(range(m)) for _ in range(n)]

        visited = [[False]*n for _ in range(m)]
        dq = deque()
        # Start at (0,0) with distance = 1
        visited[0][0] = True
        dq.append((0, 0, 1))
        # Remove (0,0) from availability
        row_avail[0].pop(0)
        col_avail[0].pop(0)

        while dq:
            r, c, d = dq.popleft()
            if r == m-1 and c == n-1:
                return d
            steps = grid[r][c]
            # Right moves
            low_c = c+1
            high_c = min(n-1, c+steps)
            row_list = row_avail[r]
            L = bisect.bisect_left(row_list, low_c)
            R = L
            # collect candidates
            while R < len(row_list) and row_list[R] <= high_c:
                nc = row_list[R]
                if not visited[r][nc]:
                    visited[r][nc] = True
                    dq.append((r, nc, d+1))
                    # remove r from column availability
                    col_list = col_avail[nc]
                    idx = bisect.bisect_left(col_list, r)
                    if idx < len(col_list) and col_list[idx] == r:
                        col_list.pop(idx)
                R += 1
            # remove processed columns from this row
            del row_list[L:R]

            # Down moves
            low_r = r+1
            high_r = min(m-1, r+steps)
            col_list = col_avail[c]
            L = bisect.bisect_left(col_list, low_r)
            R = L
            while R < len(col_list) and col_list[R] <= high_r:
                nr = col_list[R]
                if not visited[nr][c]:
                    visited[nr][c] = True
                    dq.append((nr, c, d+1))
                    # remove c from row availability
                    row_list2 = row_avail[nr]
                    idx = bisect.bisect_left(row_list2, c)
                    if idx < len(row_list2) and row_list2[idx] == c:
                        row_list2.pop(idx)
                R += 1
            del col_list[L:R]

        return -1