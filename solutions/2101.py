from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        # Helper: can cross on day d (1-based days, d=0 means no water yet)
        def can(d):
            # build water grid
            flooded = [[False]*col for _ in range(row)]
            for i in range(d):
                r, c = cells[i]
                flooded[r-1][c-1] = True

            # BFS from all land in top row
            q = deque()
            seen = [[False]*col for _ in range(row)]
            for c0 in range(col):
                if not flooded[0][c0]:
                    q.append((0, c0))
                    seen[0][c0] = True

            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                r0, c0 = q.popleft()
                if r0 == row-1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r0+dr, c0+dc
                    if 0 <= nr < row and 0 <= nc < col and not flooded[nr][nc] and not seen[nr][nc]:
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return False

        n = len(cells)
        lo, hi = 0, n
        # binary search for max day
        while lo < hi:
            mid = (lo + hi + 1)//2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
