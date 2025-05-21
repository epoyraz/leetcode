from collections import deque

class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        # dist[r][c] = min obstacles removed to reach (r,c)
        dist = [ [float('inf')] * n for _ in range(m) ]
        dist[0][0] = 0
        
        dq = deque([(0, 0)])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while dq:
            r, c = dq.popleft()
            d = dist[r][c]
            # Early exit if we've reached the goal
            if r == m-1 and c == n-1:
                return d
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nd = d + grid[nr][nc]
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        # 0-1 BFS: zeroâcost edge to front, costâ1 edge to back
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        
        # In case the loop ends without early return
        return dist[m-1][n-1]
