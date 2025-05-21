from collections import deque

class Solution(object):
    def minimumMoves(self, grid):
        n = len(grid)
        # state: (r, c, orient) orient: 0=horizontal (tail at r,c, head at r,c+1), 1=vertical (tail at r,c, head at r+1,c)
        start = (0, 0, 0)
        target = (n-1, n-2, 0)
        seen = set([start])
        dq = deque([(start, 0)])
        while dq:
            (r, c, o), d = dq.popleft()
            if (r, c, o) == target:
                return d
            # move right
            if o == 0:
                # horizontal: head at (r, c+1), new tail at (r, c+1), new head at (r, c+2)
                if c+2 < n and grid[r][c+2] == 0:
                    nxt = (r, c+1, 0)
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, d+1))
            else:
                # vertical: head at (r+1, c), new tail at (r, c+1)
                if c+1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
                    nxt = (r, c+1, 1)
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, d+1))
            # move down
            if o == 0:
                # horizontal: tail at (r,c),(r,c+1) -> new tail at (r+1,c),(r+1,c+1)
                if r+1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0:
                    nxt = (r+1, c, 0)
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, d+1))
            else:
                # vertical: tail at (r,c),(r+1,c) -> new tail at (r+1,c),(r+2,c)
                if r+2 < n and grid[r+2][c] == 0:
                    nxt = (r+1, c, 1)
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, d+1))
            # rotate clockwise
            if o == 0:
                # horizontal -> vertical around tail: need cells (r+1,c) and (r+1,c+1)
                if r+1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0:
                    nxt = (r, c, 1)
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, d+1))
            else:
                # rotate counterclockwise: vertical -> horizontal around tail: need cells (r,c+1) and (r+1,c+1)
                if c+1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
                    nxt = (r, c, 0)
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, d+1))
        return -1