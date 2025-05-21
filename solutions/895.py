class Solution(object):
    def shortestPathAllKeys(self, grid):
        m = len(grid)
        n = len(grid[0])
        all_keys = 0
        sx = sy = 0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    sx, sy = i, j
                elif 'a' <= c <= 'f':
                    all_keys |= 1 << (ord(c) - ord('a'))
        from collections import deque
        q = deque([(sx, sy, 0, 0)])
        visited = [[[False] * (1<<6) for _ in range(n)] for _ in range(m)]
        visited[sx][sy][0] = True
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y, mask, steps = q.popleft()
            if mask == all_keys:
                return steps
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    c = grid[nx][ny]
                    if c == '#':
                        continue
                    new_mask = mask
                    if 'a' <= c <= 'f':
                        new_mask |= 1 << (ord(c) - ord('a'))
                    if 'A' <= c <= 'F':
                        if not mask & (1 << (ord(c) - ord('A'))):
                            continue
                    if not visited[nx][ny][new_mask]:
                        visited[nx][ny][new_mask] = True
                        q.append((nx, ny, new_mask, steps + 1))
        return -1
