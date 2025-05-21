from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        # Step 1: multi-source BFS to compute distance to nearest thief
        dist = [[-1]*n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i,j))

        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Step 2: max-heap Dijkstra to find path with max min-distance (safeness factor)
        heap = [(-dist[0][0], 0, 0)]
        visited = [[False]*n for _ in range(n)]

        while heap:
            d, x, y = heapq.heappop(heap)
            d = -d
            if x == n-1 and y == n-1:
                return d
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(heap, (-min(d, dist[nx][ny]), nx, ny))
