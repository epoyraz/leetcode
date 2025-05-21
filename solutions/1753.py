import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        # dist[r][c] = minimum possible "max-edge" effort to reach (r,c)
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        
        # Min-heap of (effort_so_far, r, c)
        heap = [(0, 0, 0)]
        seen = [[False]*cols for _ in range(rows)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)
            if seen[r][c]:
                continue
            seen[r][c] = True
            # If we've reached the target, this is the minimal effort
            if r == rows-1 and c == cols-1:
                return effort
            
            # Explore neighbors
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not seen[nr][nc]:
                    # Edge cost is the height difference
                    cost = abs(heights[nr][nc] - heights[r][c])
                    # New path effort is the max of current path effort and this edge
                    new_effort = max(effort, cost)
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        
        # Fallback (should never hit this if the grid is connected)
        return dist[rows-1][cols-1]
