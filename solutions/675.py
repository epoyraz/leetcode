from collections import deque

class Solution(object):
    def cutOffTree(self, forest):
        if not forest or not forest[0]:
            return -1
        
        m, n = len(forest), len(forest[0])
        trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        
        def bfs(sx, sy, tx, ty):
            if sx == tx and sy == ty:
                return 0
            visited = [[False] * n for _ in range(m)]
            queue = deque([(sx, sy, 0)])
            visited[sx][sy] = True
            while queue:
                x, y, d = queue.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and forest[nx][ny] != 0:
                        if nx == tx and ny == ty:
                            return d + 1
                        visited[nx][ny] = True
                        queue.append((nx, ny, d + 1))
            return -1
        
        sx = sy = 0
        total_steps = 0
        for h, tx, ty in trees:
            steps = bfs(sx, sy, tx, ty)
            if steps == -1:
                return -1
            total_steps += steps
            sx, sy = tx, ty
        
        return total_steps
