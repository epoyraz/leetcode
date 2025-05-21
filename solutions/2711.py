import heapq

class Solution(object):
    def minimumTime(self, grid):
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        heap = [(0, 0, 0)]  # (time, row, col)
        visited = [[False]*n for _ in range(m)]
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        while heap:
            time, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True

            if r == m - 1 and c == n - 1:
                return time

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    wait_time = max(grid[nr][nc], time + 1)
                    # adjust for even-odd parity trap
                    if (wait_time - time) % 2 == 0:
                        wait_time += 1
                    heapq.heappush(heap, (wait_time, nr, nc))

        return -1
