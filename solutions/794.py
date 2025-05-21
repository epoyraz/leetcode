import heapq

class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while heap:
            t, x, y = heapq.heappop(heap)
            if (x, y) == (n-1, n-1):
                return t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(heap, (max(t, grid[nx][ny]), nx, ny))
