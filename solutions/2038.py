from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        sr, sc = entrance
        visited = [[False]*n for _ in range(m)]
        visited[sr][sc] = True
        q = deque([(sr, sc, 0)])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            r, c, d = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and maze[nr][nc] == '.':
                    if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:
                        return d + 1
                    visited[nr][nc] = True
                    q.append((nr, nc, d+1))
        return -1
