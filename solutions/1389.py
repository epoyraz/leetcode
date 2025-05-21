from collections import deque

class Solution:
    def minPushBox(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Find initial positions of box, target and player
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sx, sy = i, j
                elif grid[i][j] == 'B':
                    bx, by = i, j
                elif grid[i][j] == 'T':
                    tx, ty = i, j

        # Check if player can reach (px, py) from (sx, sy) without crossing box
        def can_reach(sx, sy, px, py, bx, by):
            visited = [[False]*n for _ in range(m)]
            queue = deque([(sx, sy)])
            visited[sx][sy] = True
            while queue:
                x, y = queue.popleft()
                if x == px and y == py:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != '#' and (nx, ny) != (bx, by):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False

        # BFS on box pushes
        visited = set()
        queue = deque()
        queue.append((bx, by, sx, sy, 0))  # box_x, box_y, player_x, player_y, pushes
        visited.add((bx, by, sx, sy))

        while queue:
            bx, by, px, py, pushes = queue.popleft()
            if (bx, by) == (tx, ty):
                return pushes
            for dx, dy in directions:
                nbx, nby = bx + dx, by + dy  # new box position
                ppx, ppy = bx - dx, by - dy  # required player position to push
                if 0 <= nbx < m and 0 <= nby < n and 0 <= ppx < m and 0 <= ppy < n:
                    if grid[nbx][nby] == '#' or grid[ppx][ppy] == '#':
                        continue
                    if not can_reach(px, py, ppx, ppy, bx, by):
                        continue
                    if (nbx, nby, bx, by) in visited:
                        continue
                    visited.add((nbx, nby, bx, by))
                    queue.append((nbx, nby, bx, by, pushes + 1))

        return -1
